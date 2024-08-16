from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)
from rest_framework import generics, mixins
from rest_framework.views import APIView
from users.authentication import JWTAuthentication
from .models import Exercice
from .serializer import ExerciceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from django.core.files.storage import default_storage
from rest_framework.response import Response


class ProgramGenericAPIView(generics.GenericAPIView, 
                            mixins.ListModelMixin, 
                            mixins.RetrieveModelMixin, 
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin, 
                            mixins.DestroyModelMixin):
    queryset = Exercice.objects.all()
    serializer_class = ExerciceSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class FileUploadView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)

    def post(self, request):
        logger.debug(f"request.FILES: {request.FILES}")
        logger.debug(f"request.data: {request.data}")

        file = request.FILES.get('File')
        if not file:
            return Response({'error': 'No file provided or key "File" is missing'}, status=400)
    
        file_name = default_storage.save(file.name, file)
        url = default_storage.url(file_name)

        return Response({
            'url': 'http://localhost:8000/api' + url
        })
