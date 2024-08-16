from django.db import models

class Programs(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    duree = models.CharField(max_length=50)
    coach = models.ForeignKey('users.Coach', on_delete=models.CASCADE, related_name='programmes')
    # client = models.ForeignKey('users.Client', on_delete=models.CASCADE, related_name='programmes')
