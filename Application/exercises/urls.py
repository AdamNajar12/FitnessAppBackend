from django.urls import path
from .views import ProgramGenericAPIView,FileUploadView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('exercice/', ProgramGenericAPIView.as_view(), name='exercice-list'),
    path('exercice/<int:pk>/', ProgramGenericAPIView.as_view(), name='exercice-detail'),
    path('upload', FileUploadView.as_view())
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

