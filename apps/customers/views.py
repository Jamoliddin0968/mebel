from django.shortcuts import render
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework import viewsets

from drf_spectacular.utils import extend_schema


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    http_method_names = ['get', 'post', 'put', 'patch']

    @extend_schema(
        tags=['Customer'],
        description='Retrieve all customers'
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Customer'],
        description='Create a new customer'
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Customer'],
        description='Retrieve a specific customer by ID'
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Customer'],
        description='Update a specific customer by ID'
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Customer'],
        description='Partially update a specific customer by ID'
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
