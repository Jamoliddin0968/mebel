from rest_framework.serializers import ModelSerializer

from .models import (Product, Stock,)


class ProductSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Product


class StockSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Stock
