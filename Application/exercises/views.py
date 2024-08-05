from django.shortcuts import render

from rest_framework import generics, mixins
from .models import Exercice
from .serializer import ExerciceSerializer

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

