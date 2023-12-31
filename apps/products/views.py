from drf_spectacular.utils import extend_schema_view
from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, DestroyAPIView

from rest_framework import status
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('product_images').all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    @extend_schema(
        tags=['Product'],
        description='Retrieve all products'
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Product'],
        description='Create a new product'
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Product'],
        description='Retrieve a specific product by ID'
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Product'],
        description='Update a specific product by ID'
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Product'],
        description='Partially update a specific product by ID'
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


@extend_schema_view(
    create=extend_schema(tags=["Product Images"]),
    destroy=extend_schema(tags=["Product Images"])
)
class ProductImageViewset(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    http_method_names = ["post", "delete"]
