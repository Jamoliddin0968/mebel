from rest_framework import serializers

from .models import WareHouse, WareHouseItem


class WareHouseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WareHouseItem
        fields = '__all__'


class WareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WareHouse
        fields = '__all__'
