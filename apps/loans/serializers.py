from rest_framework import serializers
from .models import Loans


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = "__all__"
