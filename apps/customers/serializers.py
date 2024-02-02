from rest_framework.serializers import ModelSerializer
from .models import Customer
from rest_framework.serializers import IntegerField


class CustomerSerializer(ModelSerializer):
    # loan = IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = "__all__"
