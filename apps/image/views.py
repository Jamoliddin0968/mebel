from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .models import Image
from .serializers import ImagesSerializer


class ImageCreateAPIView(CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImagesSerializer
