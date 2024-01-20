from rest_framework import serializers

from apps.branches.serializers import BranchSerializer
from apps.products.serializers import ProductSerializer

from .models import WareHouse


class WareHouseSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()

    class Meta:
        model = WareHouse
        fields = '__all__'
