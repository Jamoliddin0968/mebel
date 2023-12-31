from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Notification

        extra_kwargs = {
            'user': {'read_only': True}
        }
