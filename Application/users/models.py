from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=[('coach', 'Coach'), ('client', 'Client')])
    username = None 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Custom related name to avoid conflicts
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Custom related name to avoid conflicts
        blank=True
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Coach(User):
    specialite = models.CharField(max_length=50)
    review = models.IntegerField(default=0)

class Client(User):
    age = models.IntegerField()
    poids = models.FloatField()
    objectifs = models.TextField()
    taille = models.FloatField()
    niveau = models.CharField(max_length=30)
    programmes = models.ManyToManyField('programs.Programs', related_name='clients', blank=True)