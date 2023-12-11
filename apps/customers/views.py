from django.shortcuts import render
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    http_method_names = ['get', 'post', 'put']
