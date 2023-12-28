from rest_framework import viewsets
from .models import Sale
from .serializers import SaleSerializer
from drf_spectacular.utils import extend_schema


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    http_method_names = ["get", "post", "delete"]

    @extend_schema(
        tags=['Sale'],
        description='Retrieve all sales'
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Sale'],
        description='Create a new sale'
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Sale'],
        description='Delete a specific sale by ID'
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
