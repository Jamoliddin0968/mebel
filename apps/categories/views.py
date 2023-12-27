from .models import Category
from .serializers import CategorySerializer
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.select_related('category_products').all()
    serializer_class = CategorySerializer

    http_method_names = ['get', 'post', 'put', 'patch']

    @extend_schema(
        tags=['Category'],
        description='Retrieve all categories'
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Category'],
        description='Create a new category'
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Category'],
        description='Retrieve a specific category by ID'
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Category'],
        description='Update a specific category by ID'
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Category'],
        description='Partially update a specific category by ID'
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
