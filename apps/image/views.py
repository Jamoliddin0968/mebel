from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView

from .models import Image
from .serializers import ImagesSerializer


class ImageCreateAPIView(CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImagesSerializer


class ImageListAPIView(ListAPIView):
    queryset = Image.objects.order_by('-id').all()[:8]
    serializer_class = ImagesSerializer
