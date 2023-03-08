from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
# Create your views here.
from rest_framework.generics import ListAPIView

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer