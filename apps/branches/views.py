from rest_framework import viewsets
from .models import Branch

from .serializers import BranchSerializer

from drf_spectacular.utils import extend_schema_view,extend_schema


@extend_schema_view(
    list=extend_schema(tags=["Branches"]),
    retrieve=extend_schema(tags=["Branches"]),
    create=extend_schema(tags=["Branches"]),
    update=extend_schema(tags=["Branches"]),
    partial_update=extend_schema(tags=["Branches"]),
    destroy=extend_schema(tags=["Branches"])
)
class BranchViewSet(viewsets.ModelViewSet):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()

    http_method_names = ['get', 'post', 'put', 'patch']
