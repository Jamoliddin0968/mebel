from .models import Category
from .serializers import CategorySerializer

from rest_framework import viewsets, mixins


class CategoryViewSet(mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.select_related('category_products').all()
    serializer_class = CategorySerializer

    http_method_names = ['get', 'post', 'put']
