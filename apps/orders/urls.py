from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register("", OrderViewSet)
router.register("images", OrderImageViewSet)
router.register('full', FullOrderViewSet)
router.register("items", OrderItemViewSet)
urlpatterns = [
    path("", include(router.urls), name="orders"),
    path("<int:pk>/view_date", ViewDateApiView.as_view(), name="View_dateapi"),
    path("<int:pk>/end_date", EndDateApiView.as_view(), name="end_dateapi"),
    path("<int:pk>/completion", CompletionDateApiView.as_view(),
         name="Completion_dateapi"),
    path("<int:pk>/status", StatusApiView.as_view(), name="status"),
]
