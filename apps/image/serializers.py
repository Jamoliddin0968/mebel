from rest_framework.serializers import ModelSerializer

from .models import Image


class ImagesSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
