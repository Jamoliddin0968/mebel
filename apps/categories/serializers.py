from rest_framework.serializers import ModelSerializer

from apps.products.serializers import ProductSerializer

from .models import Category


class CategorySerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Category
