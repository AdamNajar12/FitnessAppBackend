from django.db import models

from users.models import Coach, Client

class Programs(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    duree = models.IntegerField()  # durée en jours
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='programmes')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='programmes')

# Create your models here.
