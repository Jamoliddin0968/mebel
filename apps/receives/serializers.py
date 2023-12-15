from rest_framework import serializers
from apps.receives.models import Receive


class ReceiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receive
        fields = "__all__"
