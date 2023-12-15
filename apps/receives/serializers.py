from rest_framework import serializers
from apps.receives.models import Receive
from apps.warehouses.models import WareHouse


class ReceiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receive
        fields = "__all__"

    def create(self, validated_data):
        obj = super().create(validated_data)
        amount = obj.amount
        product = obj.product
        branch = obj.branch
        warehouse_item, _ = WareHouse.objects.get_or_create(
            product=product, branch=branch)
        warehouse_item.amount += amount
        warehouse_item.save()
        return obj
