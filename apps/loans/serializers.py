from rest_framework import serializers
from .models import Loans


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = "__all__"

        extra_kwargs = {
            'user': {'read_only': True}
        }