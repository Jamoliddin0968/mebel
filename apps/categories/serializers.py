from rest_framework.serializers import ModelSerializer
from apps.products.serializers import ProductSerializer
from .models import Category


class CategorySerializer(ModelSerializer):
    products = ProductSerializer(
        many=True, source="category_products", read_only=True)

    class Meta:
        fields = "__all__"
        model = Category
