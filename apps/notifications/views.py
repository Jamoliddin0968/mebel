from rest_framework import viewsets
from apps.notifications.models import Notification
from drf_spectacular.utils import extend_schema
from apps.notifications.serializers import NotificationSerializer
from drf_spectacular.utils import extend_schema_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .serializers import ScheduledLoanSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,]

    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        tags=['Notification'],
        description='Retrieve all notifications'
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Notification'],
        description='Create a new notification'
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Notification'],
        description='Retrieve a specific notification by ID'
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Notification'],
        description='Update a specific notification by ID'
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Notification'],
        description='Partial update of a specific notification by ID'
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Notification'],
        description='Delete a specific notification by ID'
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

