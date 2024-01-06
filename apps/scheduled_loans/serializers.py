from rest_framework import serializers
from .models import ScheduledLoan

from apps.notifications.serializers import ScheduledNotificationSerializer


class ScheduledLoanSerializer(serializers.ModelSerializer):
    sheduled_notification = ScheduledNotificationSerializer(
        many=True, read_only=True)

    class Meta:
        fields = "__all__"
        model = ScheduledLoan
