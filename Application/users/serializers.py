from rest_framework import serializers
from .models import User, Coach, Client

class UserSerializer(serializers.ModelSerializer):
    confirmPassword = serializers.CharField(write_only=True)
    role = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'nom', 'prenom', 'telephone', 'role', 'password', 'confirmPassword'] 
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirmPassword')
        user = User.objects.create_user(**validated_data)
        return user 

class CoachSerializer(serializers.ModelSerializer):
    confirmPassword = serializers.CharField(write_only=True)
    role = serializers.CharField()

    class Meta:
        model = Coach
        fields = ['email', 'nom', 'prenom', 'telephone', 'role', 'password', 'confirmPassword', 'specialite', 'review']

    def validate(self, data):
        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirmPassword')
        coach = Coach.objects.create_user(**validated_data)
        return coach

class ClientSerializer(serializers.ModelSerializer):
    confirmPassword = serializers.CharField(write_only=True)
    role = serializers.CharField()

    class Meta:
        model = Client
        fields = ['email', 'nom', 'prenom', 'telephone', 'role', 'password', 'confirmPassword', 'age', 'poids', 'objectifs', 'taille']

    def validate(self, data):
        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirmPassword')
        client = Client.objects.create_user(**validated_data)
        return client
