from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ReceiveSerializer
from .models import Receive
from rest_framework.permissions import IsAuthenticated


class ReceiveViewSet(viewsets.ModelViewSet):
    queryset = Receive.objects.all()
    serializer_class = ReceiveSerializer

    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
