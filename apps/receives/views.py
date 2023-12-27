from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ReceiveItemSerializer, ReceiveSerializer
from .models import Receive, ReceiveItem
from rest_framework.permissions import IsAuthenticated


class ReceiveViewSet(viewsets.ModelViewSet):
    queryset = Receive.objects.all()
    serializer_class = ReceiveSerializer

    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReceiveItemViewSet(viewsets.ModelViewSet):
    queryset = ReceiveItem.objects.all()
    serializer_class = ReceiveItemSerializer
    permission_classes = [IsAuthenticated,]
    http_method_names = ["delete", "patch"]
