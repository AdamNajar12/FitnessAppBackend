from django.urls import path
from .views import ProgramGenericAPIView

urlpatterns = [
    path('programs/', ProgramGenericAPIView.as_view(), name='program-list'),
    path('programs/<int:pk>/', ProgramGenericAPIView.as_view(), name='program-detail'),
]
