from django.db import models
from programs.models import Programs
from users.models import Client

class Exercice(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    duree = models.CharField()  # durée en minutes
    repetitions = models.IntegerField()
    sets = models.IntegerField()
    verrouillage = models.BooleanField(default=False)
    file = models.CharField(max_length=200)
    programme = models.ForeignKey(Programs, on_delete=models.CASCADE, related_name='exercices')

class Progression(models.Model):
    date = models.DateField()
    note = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='progressions')
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE, related_name='progressions')
