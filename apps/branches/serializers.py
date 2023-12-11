from rest_framework.serializers import ModelSerializer, CharField
from .models import Branch


class BranchSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"
