from drf_spectacular.openapi import OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from rest_framework import viewsets

from .models import WareHouse
from .serializers import WareHouseSerializer

from drf_spectacular.utils import extend_schema, extend_schema_view
@extend_schema_view(
    list=extend_schema(tags=["Warehouse"]),
    retrieve=extend_schema(tags=["Warehouse"]),
    create=extend_schema(tags=["Warehouse"]),
    update=extend_schema(tags=["Warehouse"]),
    partial_update=extend_schema(tags=["Warehouse"]),
    destroy=extend_schema(tags=["Warehouse"])
)
class WareHouseViewSet(viewsets.ModelViewSet):
    queryset = WareHouse.objects.all()
    serializer_class = WareHouseSerializer

    http_method_names = ["get",]

    @extend_schema(tags=["Warehouse"],
                   parameters=[
        OpenApiParameter(
            name='karimjon_id', description='Karimjon Id', type=OpenApiTypes.INT),
    ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
