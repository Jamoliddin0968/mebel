from rest_framework import serializers
from .models import ScheduledLoan


class ScheduledLoanSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ScheduledLoan
