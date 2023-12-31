from rest_framework import viewsets
from .models import Sale
from .serializers import SaleSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@extend_schema_view(
    list=extend_schema(tags=["Sales"]),
    retrieve=extend_schema(tags=["Sales"]),
    create=extend_schema(tags=["Sales"]),
    update=extend_schema(tags=["Sales"]),
    partial_update=extend_schema(tags=["Sales"]),
    destroy=extend_schema(tags=["Sales"])
)
class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    http_method_names = ["get", "post", "delete"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
