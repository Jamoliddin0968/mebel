from drf_spectacular.openapi import OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from .models import WareHouseItem
from .serializers import WareHouseItemCreateSerializer, WareHouseItemSerializer


@extend_schema_view(
    create=extend_schema(tags=["Warehouse-items"]),
    partial_update=extend_schema(tags=["Warehouse-items"]),
    list=extend_schema(tags=["Warehouse-items"]),
    retrieve=extend_schema(tags=["Warehouse-items"]),
)
class WareHouseItemViewSet(viewsets.ModelViewSet):
    queryset = WareHouseItem.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'partial_update':
            return WareHouseItemCreateSerializer
        return WareHouseItemSerializer

    http_method_names = ['get', 'post', 'patch']
