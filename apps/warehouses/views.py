from rest_framework import viewsets
from .models import WareHouse, WareHouseItem
from .serializers import WareHouseSerializer, WareHouseItemSerializer

from drf_spectacular.utils import extend_schema

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.openapi import OpenApiParameter


class WareHouseViewSet(viewsets.ModelViewSet):
    queryset = WareHouse.objects.prefetch_related('warehouseitem_set').all()
    serializer_class = WareHouseSerializer

    http_method_names = ["get",]

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category_id')
        branch_id = self.request.query_params.get('branch_id')

        if category_id:
            queryset = queryset.filter(
                warehouseitem__product__category_id=category_id)
        if branch_id:
            queryset = queryset.filter(branch_id=branch_id)

        return queryset

    @extend_schema(tags=["Warehouse"],
                   parameters=[
        OpenApiParameter(
            name='category_id', description='Category Id', type=OpenApiTypes.INT),
        OpenApiParameter(
            name='branch_id', description='Branch Id', type=OpenApiTypes.INT),
    ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class WareHouseItemViewSet(viewsets.ModelViewSet):
    queryset = WareHouseItem.objects.all()
    serializer_class = WareHouseItemSerializer

    http_method_names = ["post", "patch"]

    @extend_schema(
        tags=['Warehouse Item'],
        description='Create a new warehouse item'
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Warehouse Item'],
        description='Partially update a specific warehouse item by ID'
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
