from rest_framework import viewsets
from .models import Branch

from .serializers import BranchSerializer


class BranchViewSet(viewsets.ModelViewSet):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()

    # http_method_names = ['get', 'post', 'put', 'delete',]
