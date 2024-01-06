from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Order, OrderImage, EMPTY, NOT_FILLED, NOT_INSTALLED, IN_PROGRESS, OrderItem

from apps.notifications.models import ScheduledNotification
from apps.utils.messages import get_order_message


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderImageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = OrderImage


class OrderSerializer(serializers.ModelSerializer):
    order_images = OrderImageSerializer(many=True, read_only=True)

    class Meta:
        fields = "__all__"
        model = Order


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("customer", "branch", "user")
        model = Order

        extra_kwargs = {
            'user': {'read_only': True}
        }


class ViewDateSerializer(serializers.Serializer):
    view_date = serializers.DateField()

    def update(self, instance, validated_data):
        if instance.state == EMPTY:
            instance.view_date = validated_data.get('view_date')
            instance.state = NOT_FILLED

            obj = ScheduledNotification.objects.create(
                message=get_order_message(instance.id, instance.customer.name))
            instance.notification = obj
            instance.save()

            return instance
        else:
            raise ValidationError(detail="Not update")


class EndDateSerializer(serializers.Serializer):
    end_date = serializers.DateField()

    def update(self, instance, validated_data):
        if instance.state == NOT_FILLED:
            instance.end_date = validated_data.get('end_date')
            instance.state = NOT_INSTALLED

            obj = ScheduledNotification.objects.create(
                message=get_order_message(instance.id, instance.customer.name))
            instance.notification = obj
            instance.save()

            return instance
        else:
            raise ValidationError(detail="Not update")


class CompletionDateSerializer(serializers.Serializer):
    completion_date = serializers.DateField()

    def update(self, instance, validated_data):
        if instance.state == NOT_INSTALLED:
            instance.completion_date = validated_data.get('completion_date')

            obj = ScheduledNotification.objects.create(
                message=get_order_message(instance.id, instance.customer.name))
            instance.notification = obj
            instance.save()

            return instance
        else:
            raise ValidationError(detail="Not update")


class StateSerializer(serializers.Serializer):
    state = serializers.DateField()

    def update(self, instance, validated_data):
        if instance.state == NOT_INSTALLED:
            instance.state = validated_data.get('state')

            obj = ScheduledNotification.objects.create(
                message=get_order_message(instance.id, instance.customer.name))
            instance.notification = obj
            instance.save()

            return instance
        else:
            raise ValidationError(detail="Not update")
