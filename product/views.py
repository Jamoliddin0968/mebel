from django.shortcuts import render
from .models import Product , Stock
from .serializers import ProductSerializer ,StockSerializer
# Create your views here.
from rest_framework.generics import ListCreateAPIView

class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductListView(ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer