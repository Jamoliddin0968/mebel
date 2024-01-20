from drf_spectacular.openapi import OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from .models import WareHouse, WareHouseItem
from .serializers import (WareHouseItemCreateSerializer,
                          WareHouseItemSerializer, WareHouseSerializer)


@extend_schema_view(
    list=extend_schema(tags=["Watehouse"]),
    retrieve=extend_schema(tags=["Watehouse"]),
    create=extend_schema(tags=["Watehouse"]),
    update=extend_schema(tags=["Watehouse"]),
    partial_update=extend_schema(tags=["Watehouse"]),
    destroy=extend_schema(tags=["Watehouse"])
)
class WareHouseViewSet(viewsets.ModelViewSet):
    queryset = WareHouse.objects.all()
    serializer_class = WareHouseSerializer

    http_method_names = ["get",]

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category_id')

        if category_id:
            queryset = queryset.filter(
                warehouseitem__product__category_id=category_id)
        return queryset

    @extend_schema(tags=["Warehouse"],
                   parameters=[
        OpenApiParameter(
            name='category_id', description='Category Id', type=OpenApiTypes.INT),
    ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


@extend_schema_view(

    create=extend_schema(tags=["Warehouse-items"]),

    partial_update=extend_schema(tags=["Warehouse-items"]),
)
class WareHouseItemCreateViewSet(viewsets.ModelViewSet):
    queryset = WareHouseItem.objects.all()
    serializer_class = WareHouseItemCreateSerializer

    http_method_names = ["post", "patch"]


@extend_schema_view(
    list=extend_schema(tags=["Warehouse-items"]),
    retrieve=extend_schema(tags=["Warehouse-items"]),
)
class WareHouseItemViewSet(viewsets.ModelViewSet):
    queryset = WareHouseItem.objects.all()
    serializer_class = WareHouseItemSerializer

    http_method_names = ["post", "patch"]
