from rest_framework import viewsets
from apps.orders.models import Order, OrderImage

from apps.orders.serializers import OrderSerializer, OrderImageSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    list=extend_schema(tags=["Order"]),
    retrieve=extend_schema(tags=["Order"]),
    create=extend_schema(tags=["Order"]),
    update=extend_schema(tags=["Order"]),
    partial_update=extend_schema(tags=["Order"]),
    destroy=extend_schema(tags=["Order"])
)
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


@extend_schema_view(
    list=extend_schema(tags=["Order-image"]),
    retrieve=extend_schema(tags=["Order-image"]),
    create=extend_schema(tags=["Order-image"]),
    update=extend_schema(tags=["Order-image"]),
    partial_update=extend_schema(tags=["Order-image"]),
    destroy=extend_schema(tags=["Order-image"])
)
class OrderImageViewSet(viewsets.ModelViewSet):
    serializer_class = OrderImageSerializer
    queryset = OrderImage.objects.all()
