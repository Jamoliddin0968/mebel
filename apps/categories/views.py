from .models import Category
from .serializers import CategorySerializer
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins

from drf_spectacular.utils import extend_schema, extend_schema_view
@extend_schema_view(
    list=extend_schema(tags=['Category']),
    retrieve=extend_schema(tags=['Category']),
    create=extend_schema(tags=['Category']),
    update=extend_schema(tags=['Category']),
    partial_update=extend_schema(tags=['Category']),
    destroy=extend_schema(tags=['Category'])
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch']

