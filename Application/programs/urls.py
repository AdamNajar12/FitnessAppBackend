from django.urls import path
from .views import ProgramGenericAPIView,CoachStatisticsView,NewClientsPerMonthView, GetClientsByCoach,get_programs_by_coach,get_clients_by_program

urlpatterns = [
    path('programs/', ProgramGenericAPIView.as_view(), name='program-list'),
    path('programs/<int:pk>/', ProgramGenericAPIView.as_view(), name='program-detail'),
    path('coach-statistics/', CoachStatisticsView.as_view(), name='coach_statistics'),
    path('new-clients-per-month/', NewClientsPerMonthView.as_view(), name='new-clients-per-month'),
    path('coach/clients/', GetClientsByCoach.as_view(), name='clients_by_coach'),
    path('ProgrambyCoachAuth/', get_programs_by_coach.as_view()),
    path('ClientbyProgram', get_clients_by_program.as_view()),
]
