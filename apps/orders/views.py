from rest_framework import viewsets
from apps.orders.models import Order, OrderImage
from rest_framework.generics import UpdateAPIView
from apps.orders.serializers import *
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.response import Response


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


class ViewDateApiView(UpdateAPIView):
    serializer_class = ViewDateSerializer
    queryset = Order.objects.all()


class EndDateApiView(UpdateAPIView):
    serializer_class = EndDateSerializer
    queryset = Order.objects.all()


class CompletionDateApiView(UpdateAPIView):
    serializer_class = CompletionDateSerializer
    queryset = Order.objects.all()


class StatusApiView(UpdateAPIView):
    serializer_class = StateSerializer
    queryset = Order.objects.all()


@extend_schema_view(
    list=extend_schema(tags=["FullOrder"]),
    retrieve=extend_schema(tags=["FullOrder"]),
    create=extend_schema(tags=["FullOrder"]),
    update=extend_schema(tags=["FullOrder"]),
    partial_update=extend_schema(tags=["FullOrder"]),
    destroy=extend_schema(tags=["FullOrder"])
)
class FullOrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    http_method_names = ["get"]


@extend_schema_view(
    list=extend_schema(tags=["OrderItem"]),
    retrieve=extend_schema(tags=["OrderItem"]),
    create=extend_schema(tags=["OrderItem"]),
    update=extend_schema(tags=["OrderItem"]),
    partial_update=extend_schema(tags=["OrderItem"]),
    destroy=extend_schema(tags=["OrderItem"])
)
class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
