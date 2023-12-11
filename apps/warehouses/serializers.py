from rest_framework.serializers import ModelSerializer, CharField
from .models import WareHouse


class WareHouseSerializer(ModelSerializer):
    class Meta:
        model = WareHouse
        fields = "__all__"
