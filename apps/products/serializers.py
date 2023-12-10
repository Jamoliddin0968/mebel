from rest_framework.serializers import ModelSerializer, IntegerField

from .models import (Product, ProductImage)


class ProductSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Product


class ProductImageSerializer(ModelSerializer):
    product = IntegerField(read_only=True)

    class Meta:
        fields = "__all__"
        model = ProductImage
