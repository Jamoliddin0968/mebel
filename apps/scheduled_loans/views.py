from drf_spectacular.utils import extend_schema, extend_schema_view
from apps.scheduled_loans.models import ScheduledLoan

from apps.scheduled_loans.serializers import ScheduledLoanSerializer
from rest_framework import viewsets


@extend_schema_view(
    list=extend_schema(tags=["Scheduled Loans"]),
    retrieve=extend_schema(tags=["Scheduled Loans"]),
    create=extend_schema(tags=["Scheduled Loans"]),
    update=extend_schema(tags=["Scheduled Loans"]),
    partial_update=extend_schema(tags=["Scheduled Loans"]),
    destroy=extend_schema(tags=["Scheduled Loans"])
)
class ScheduledLoanViewset(viewsets.ModelViewSet):
    serializer_class = ScheduledLoanSerializer
    queryset = ScheduledLoan.objects.all()

    http_method_names = ["post", "delete", "patch"]
