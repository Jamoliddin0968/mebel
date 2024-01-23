from django.shortcuts import render
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework import viewsets

from drf_spectacular.utils import extend_schema,extend_schema_view

@extend_schema_view(
    list=extend_schema(tags=['Customers']),
    retrieve=extend_schema(tags=['Customers']),
    create=extend_schema(tags=['Customers']),
    update=extend_schema(tags=['Customers']),
    partial_update=extend_schema(tags=['Customers']),
)
class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    http_method_names = ['get', 'post', 'put', 'patch']


