from rest_framework import serializers

from apps.branches.serializers import BranchSerializer
from apps.products.serializers import ProductSerializer

from .models import WareHouseItem


class WareHouseItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WareHouseItem
        fields = '__all__'


class WareHouseItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = WareHouseItem
        fields = '__all__'
