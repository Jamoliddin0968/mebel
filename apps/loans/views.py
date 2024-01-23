from rest_framework import viewsets

from .serializers import LoanSerializer
from .models import Loans
from drf_spectacular.utils import extend_schema,extend_schema_view

from rest_framework.permissions import IsAuthenticatedOrReadOnly

@extend_schema_view(
    list=extend_schema(tags=['Loans']),
    retrieve=extend_schema(tags=['Loans']),
    create=extend_schema(tags=['Loans']),
    update=extend_schema(tags=['Loans']),
    partial_update=extend_schema(tags=['Loans']),
    destroy=extend_schema(tags=["Loans"])
)
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loans.objects.all()
    serializer_class = LoanSerializer
    http_method_names = ["post", 'patch', "get"]
    permission_classes = [IsAuthenticatedOrReadOnly,]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
