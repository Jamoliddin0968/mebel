from django.db.models import Prefetch
from rest_framework import serializers
from apps.receives.models import Receive, ReceiveItem
from apps.warehouse_items.models import WareHouseItem
from apps.warehouses.models import WareHouse


class ReceiveItemSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ("receive",)
        model = ReceiveItem

        # extra_kwargs = {
        #     'receive': {'read_only': True}
        # }

class ReceiveSerializer(serializers.ModelSerializer):
    receive_items = ReceiveItemSerializer(many=True)

    class Meta:
        model = Receive
        fields = "__all__"

        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        items = validated_data.pop('receive_items')
        obj =  super(ReceiveSerializer, self).create(validated_data)
        branch = obj.branch
        warehouse_item, _ = WareHouse.objects.get_or_create(branch=branch)
        receive_item_list = []


        for item in items:
            receive_item = ReceiveItem(**item)
            receive_item.receive = obj
            warehouse_item,_ = WareHouseItem.objects.get_or_create(product_id=item.get('product'))
            warehouse_item.amount += item.get('amount')
            warehouse_item.save()
            receive_item_list.append(receive_item)
        ReceiveItem.objects.bulk_create(receive_item_list)
        return obj
