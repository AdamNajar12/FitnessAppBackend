from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from users.authentication import JWTAuthentication
from .models import Programs
from users.models import Client,Coach
from exercises.models import Exercice
from .serializer import ProgramSerializer
from django.db.models.functions import TruncMonth
from django.db.models import Count
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view

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
        
        
        coach = user.coach
        
        # Total des programmes liés au coach
        programs = Programs.objects.filter(coach=coach)
        total_programs = programs.count()
        print(f"Total programs: {total_programs}")
        
        # Total des clients affectés à ces programmes
        clients_in_programs = Client.objects.filter(programmes__in=programs).distinct().count()
        print(f"Clients in programs: {clients_in_programs}")
        total_exercises = Exercice.objects.filter(programme__in=programs).count()
        total_clients_affected = clients_in_programs
        if total_programs > 0:
            # Calcul du pourcentage de clients affectés
            affected_clients_percentage = (clients_in_programs / total_programs) * 100
        else:
            affected_clients_percentage = 0

        data = {
            'affected_clients_percentage': round(affected_clients_percentage, 2),
            'total_programs': total_programs,
            'total_exercices':total_exercises,
            'clients_in_programs': clients_in_programs,
            'total_clients':total_clients_affected
        }

        return JsonResponse(data)

class NewClientsPerMonthView(APIView):
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Utilisez le nouveau champ pour la date d'inscription
        clients_per_month = (
            Client.objects.annotate(month=TruncMonth('date_creation'))
            .values('month')
            .annotate(count=Count('id'))
            .order_by('month')
        )

        clients_per_month_data = {str(entry['month']): entry['count'] for entry in clients_per_month}

        data = {
            'clients_per_month': clients_per_month_data,
        }

        return Response(data)



class GetClientsByCoach(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            coach = user.coach  # Vérifie que l'utilisateur est bien un coach
        except Coach.DoesNotExist:
            return Response({"error": "Coach not found."}, status=400)

        # Récupérer tous les programmes associés au coach authentifié
        programs = Programs.objects.filter(coach=coach).prefetch_related('clients')  
        client_list = []

        # Boucle sur les programmes pour obtenir les clients
        for program in programs:
            clients = program.clients.all()  # Utilisation correcte du ManyToManyField
            for client in clients:
                client_list.append({
                    'program_name': program.nom,
                    'client_name': f"{client.prenom} {client.nom}",
                })

        return Response({'clients': client_list})


class get_programs_by_coach(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        coach = user.coach
        programs = Programs.objects.filter(coach=coach)
        program_list = [{'nom': program.nom} for program in programs]

        return Response({'programs': program_list})
class get_clients_by_program(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        program_name = request.query_params.get('program_name', None)

        if not program_name:
            return Response({'error': 'Aucun programme spécifié.'}, status=400)

        try:
            program = Programs.objects.get(nom=program_name)
            clients = program.clients.all()
            client_list = [
                {'client_name': f"{client.prenom} {client.nom}", 'program_name': program.nom}
                for client in clients
            ]
            return Response({'clients': client_list}, status=200)
        except Programs.DoesNotExist:
            return Response({'error': 'Programme non trouvé.'}, status=404)
 
  