from rest_framework.serializers import ModelSerializer, IntegerField

from .models import (Product, ProductImage)
from apps.warehouses.models import WareHouse
from apps.branches.models import Branch


class ProductImageSerializer(ModelSerializer):
    # product = IntegerField(read_only=True)

    class Meta:
        fields = "__all__"
        model = ProductImage


class ProductSerializer(ModelSerializer):
    images = ProductImageSerializer(
        many=True, source='product_images', read_only=True)

    class Meta:
        fields = "__all__"
        model = Product

    def create(self, validated_data):
        new_product = super().create(validated_data)
        branches = WareHouse.objects.all()
        for branch_item in branches:
            WareHouse.objects.get_or_create(
                warehouse=branch_item, product=new_product)

        return new_product
