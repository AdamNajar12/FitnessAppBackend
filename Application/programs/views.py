from django.shortcuts import render

from rest_framework import generics, mixins
from .models import Programs
from .serializer import ProgramSerializer

class ProgramGenericAPIView(generics.GenericAPIView, 
                            mixins.ListModelMixin, 
                            mixins.RetrieveModelMixin, 
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin, 
                            mixins.DestroyModelMixin):
    queryset = Programs.objects.all()
    serializer_class = ProgramSerializer

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

