from rest_framework.generics import ListCreateAPIView
from .models import User,Provider,Customer

from .serializers import UserSerializer,ProviderSerializer,CustomerSerializer

class ProviderListView(ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    
class UserListView(ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = UserSerializer

class CustomerListView(ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = CustomerSerializer