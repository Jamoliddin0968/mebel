from rest_framework import viewsets
from .serializers import ReceiveItemSerializer, ReceiveSerializer
from .models import Receive, ReceiveItem
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from drf_spectacular.utils import extend_schema,extend_schema_view

@extend_schema_view(
    list=extend_schema(tags=['Receive']),
    retrieve=extend_schema(tags=['Receive']),
    create=extend_schema(tags=['Receive']),
    update=extend_schema(tags=['Receive']),
    partial_update=extend_schema(tags=['Receive']),
    destroy=extend_schema(tags=["Receive"]),
)
class ReceiveViewSet(viewsets.ModelViewSet):
    queryset = Receive.objects.all()
    serializer_class = ReceiveSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    http_method_names = ['get',"post"]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    

@extend_schema_view(
    destroy=extend_schema(tags=["Receive-Item"]),
    partial_update=extend_schema(tags=['Receive-Item']),
)
class ReceiveItemViewSet(viewsets.ModelViewSet):
    queryset = ReceiveItem.objects.all()
    serializer_class = ReceiveItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
    http_method_names = ["delete", "patch"]
