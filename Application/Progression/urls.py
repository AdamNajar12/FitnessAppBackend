from django.urls import path
from .views import client_progression_stats

urlpatterns = [
    path('client-progression/', client_progression_stats, name='client-progression'),
]
