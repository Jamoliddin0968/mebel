from rest_framework.serializers import ModelSerializer

from .models import Product

class ProductSerializer(ModelSerializer):
    
    class Meta:
        fields = "__all__"
        model=Product