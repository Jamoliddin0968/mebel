from rest_framework.serializers import ModelSerializer, CharField
from .models import Branch
from apps.warehouses.models import WareHouse


class BranchSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"

    def create(self, validated_data):
        new_branch = super().create(validated_data)
        a, b = WareHouse.objects.get_or_create(branch=new_branch)
        return new_branch
