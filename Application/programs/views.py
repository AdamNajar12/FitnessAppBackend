from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from users.authentication import JWTAuthentication
from .models import Programs
from users.models import Client
from .serializer import ProgramSerializer
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.decorators import method_decorator

class ProgramGenericAPIView(generics.GenericAPIView, 
                            mixins.ListModelMixin, 
                            mixins.RetrieveModelMixin, 
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin, 
                            mixins.DestroyModelMixin):
    queryset = Programs.objects.all()
    serializer_class = ProgramSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CoachStatisticsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        from programs.models import Programs  # Import local pour éviter les problèmes d'importation circulaire
        from users.models import Client
        
        user = request.user
        
        # Vérifiez que l'utilisateur est bien un coach
        if not hasattr(user, 'coach'):
            return JsonResponse({'error': 'Unauthorized'}, status=403)
        
        coach = user.coach
        
        # Total des programmes liés au coach
        programs = Programs.objects.filter(coach=coach)
        total_programs = programs.count()
        print(f"Total programs: {total_programs}")
        
        # Total des clients affectés à ces programmes
        clients_in_programs = Client.objects.filter(programmes__in=programs).distinct().count()
        print(f"Clients in programs: {clients_in_programs}")

        if total_programs > 0:
            # Calcul du pourcentage de clients affectés
            affected_clients_percentage = (clients_in_programs / total_programs) * 100
        else:
            affected_clients_percentage = 0

        data = {
            'affected_clients_percentage': round(affected_clients_percentage, 2),
            'total_programs': total_programs,
            'clients_in_programs': clients_in_programs,
        }

        return JsonResponse(data)