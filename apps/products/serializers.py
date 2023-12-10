from rest_framework.serializers import ModelSerializer, IntegerField

from .models import (Product, ProductImage)


class ProductImageSerializer(ModelSerializer):
    # product = IntegerField(read_only=True)

    class Meta:
        fields = ('id', 'image')
        model = ProductImage


class ProductSerializer(ModelSerializer):
    images = ProductImageSerializer(many=True, source='product_images')

    class Meta:
        fields = "__all__"
        model = Product
