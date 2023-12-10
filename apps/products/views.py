from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, DestroyAPIView

from rest_framework import status
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageCreateAPIView(CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductImageDestroyAPIView(DestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
