from rest_framework import serializers
from .models import Sale, SaleItem


class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True, source="sale_items")

    class Meta:
        model = Sale
        fields = "__all__"
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        items = validated_data.pop('items')
        new_sale = Sale.objects.create(**validated_data)
        new_sale_items = []
        for item in items:
            new_sale_items.append(SaleItem(**item))
        SaleItem.objects.bulk_create(new_sale_items)
        return new_sale
