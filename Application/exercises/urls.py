from django.urls import path
from .views import ProgramGenericAPIView,FileUploadView,get_exercices_by_program
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('exercice/', ProgramGenericAPIView.as_view(), name='exercice-list'),
    path('exercice/<int:pk>/', ProgramGenericAPIView.as_view(), name='exercice-detail'),
    path('P/exercices/<int:program_id>/', get_exercices_by_program, name='get_exercices_by_program'),
    path('upload', FileUploadView.as_view())
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

