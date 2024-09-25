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
    STATUS_CHOICES = [
        ('ATTEINT', 'Objectif Atteint'),
        ('EN_COURS', 'En Progression'),
        ('NON_ATTEINT', 'Objectif Non Atteint'),
    ]
    date = models.DateField()
    note = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='progressions')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE, related_name='progressions')
    def __str__(self):
        return f'{self.client} - {self.status}'
