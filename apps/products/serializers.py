from rest_framework.serializers import IntegerField, ModelSerializer

from apps.branches.models import Branch
from apps.warehouse_items.models import WareHouseItem
from apps.warehouses.models import WareHouse

from .models import Product, ProductImage


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
            WareHouseItem.objects.get_or_create(
                warehouse=branch_item, product=new_product)

        return new_product
