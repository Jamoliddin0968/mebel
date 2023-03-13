from rest_framework.serializers import ModelSerializer
from .models import User,Provider,Customer

class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"

class ProviderSerializer(ModelSerializer):
    
    class Meta:
        model = Provider
        fields = "__all__"
        
class CustomerSerializer(ModelSerializer):
    
    class Meta:
        model = Customer
        fields = "__all__"