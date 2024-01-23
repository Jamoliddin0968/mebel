from django.urls import path, include
from .views import (
    ImageCreateAPIView
)

urlpatterns = [
    path("", ImageCreateAPIView.as_view()),
]
