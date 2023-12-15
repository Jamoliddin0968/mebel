from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ReceiveSerializer
from .models import Receive


class ReceiveViewSet(viewsets.ModelViewSet):
    queryset = Receive.objects.all()
    serializer_class = ReceiveSerializer
