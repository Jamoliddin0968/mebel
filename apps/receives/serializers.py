from rest_framework import serializers
from apps.receives.models import Receive, ReceiveItem
from apps.warehouses.models import WareHouse


class ReceiveItemSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = ReceiveItem


class ReceiveSerializer(serializers.ModelSerializer):
    items = ReceiveItemSerializer(many=True, source="receive_items")

    class Meta:
        model = Receive
        fields = "__all__"

        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        items = validated_data.pop('items')
        obj = super().create(validated_data)
        amount = obj.amount
        product = obj.product
        branch = obj.branch
        warehouse_item, _ = WareHouse.objects.get_or_create(
            product=product, branch=branch)
        receive_item_list = []
        warehouse_item.amount += amount
        warehouse_item.save()

        for item in items:
            receive_item = ReceiveItem(**item)
            receive_item.receive = obj
            receive_item_list.append(receive_item)
        ReceiveItem.objects.bulk_create(receive_item_list)
        return obj
