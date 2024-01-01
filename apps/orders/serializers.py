from rest_framework import serializers

from .models import Order, OrderImage


class OrderImageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = OrderImage


class OrderSerializer(serializers.ModelSerializer):
    order_images = OrderImageSerializer(many=True, read_only=True)

    class Meta:
        fields = "__all__"
        model = Order
