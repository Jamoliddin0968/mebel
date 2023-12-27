from rest_framework import viewsets
from .serializers import ReceiveItemSerializer, ReceiveSerializer
from .models import Receive, ReceiveItem
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema


class ReceiveViewSet(viewsets.ModelViewSet):
    queryset = Receive.objects.all()
    serializer_class = ReceiveSerializer
    permission_classes = [IsAuthenticated,]

    @extend_schema(
        tags=['Receive'],
        description='Retrieve all receives'
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Receive'],
        description='Create a new receive'
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Receive'],
        description='Retrieve a specific receive by ID'
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Receive'],
        description='Update a specific receive by ID'
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Receive'],
        description='Partial update of a specific receive by ID'
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Receive'],
        description='Delete a specific receive by ID'
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ReceiveItemViewSet(viewsets.ModelViewSet):
    queryset = ReceiveItem.objects.all()
    serializer_class = ReceiveItemSerializer
    permission_classes = [IsAuthenticated,]
    http_method_names = ["delete", "patch"]

    @extend_schema(
        tags=['Receive Item'],
        description='Delete a specific receive item by ID'
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(
        tags=['Receive Item'],
        description='Partially update a specific receive item by ID'
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
