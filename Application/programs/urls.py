from django.urls import path
from .views import ProgramGenericAPIView,CoachStatisticsView

urlpatterns = [
    path('programs/', ProgramGenericAPIView.as_view(), name='program-list'),
    path('programs/<int:pk>/', ProgramGenericAPIView.as_view(), name='program-detail'),
    path('coach-statistics/', CoachStatisticsView.as_view(), name='coach_statistics')
]
