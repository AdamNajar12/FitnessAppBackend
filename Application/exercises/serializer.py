from rest_framework import serializers
from .models import Exercice
from programs.serializer import ProgramSerializer
from programs.models import Programs

class ProgramRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return ProgramSerializer(instance).data

    def to_internal_value(self, data):
        try:
            return Programs.objects.get(pk=data)
        except Programs.DoesNotExist:
            raise serializers.ValidationError("Program not found")

class ExerciceSerializer(serializers.ModelSerializer):
    programme = ProgramRelatedField(many=False, queryset=Programs.objects.all())

    class Meta:
        model = Exercice
        fields = ['id', 'nom', 'type', 'duree', 'repetitions', 'sets', 'programme']
