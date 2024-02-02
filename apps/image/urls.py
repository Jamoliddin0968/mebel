from django.urls import path, include
from .views import (
    ImageCreateAPIView,ImageListAPIView
)

urlpatterns = [
    path("", ImageCreateAPIView.as_view()),
    path("last/",ImageListAPIView.as_view())
]
