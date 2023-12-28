from rest_framework import viewsets

from .serializers import LoanSerializer
from .models import Loans
from drf_spectacular.utils import extend_schema

from rest_framework.permissions import IsAuthenticatedOrReadOnly


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loans.objects.all()
    serializer_class = LoanSerializer
    http_method_names = ["post", 'patch', "get"]
    permission_classes = [IsAuthenticatedOrReadOnly,]

    @extend_schema(
        tags=['Loan'],
        description='Create a new loan'
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Loan'],
        description='Partial update of a specific loan by ID'
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Loan'],
        description='Retrieve all loans'
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
