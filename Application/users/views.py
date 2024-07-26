from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import User, Coach, Client
from .serializers import UserSerializer, CoachSerializer, ClientSerializer
from rest_framework.permissions import IsAuthenticated

# views.py

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, exceptions


from .authentication import generate_access_token,JWTAuthentication

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    # Vérifier les valeurs reçues
    print(f"Received email: {email}")
    print(f"Received password: {password}")

    # Rechercher l'utilisateur
    user = User.objects.filter(email=email).first()
    
    if user is None:
        print("User not found")  # Log
        raise exceptions.AuthenticationFailed('User not found!')

    if not user.check_password(password):
        print("Password is incorrect")  # Log
        raise exceptions.AuthenticationFailed('Incorrect Password!')

    # Créer une réponse
    response = Response()
    
    # Générer le token
    token = generate_access_token(user)
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }

    return response
class SomeProtectedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        data = UserSerializer(request.user).data
        
        return Response({
            'data': data
        })
    
    
    
class GetCurrentUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({
            'email': user.email,
            'role': user.role,
            'nom': user.nom,
            'prenom': user.prenom,
            'telephone': user.telephone,
        })




class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CoachView(generics.CreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

class ClientView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer



# Create your views here.
