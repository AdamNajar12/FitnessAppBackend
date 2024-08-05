from django.urls import path
from .views import ProgramGenericAPIView

urlpatterns = [
    path('exercice/', ProgramGenericAPIView.as_view(), name='exercice-list'),
    path('exercice/<int:pk>/', ProgramGenericAPIView.as_view(), name='exercice-detail'),
]
