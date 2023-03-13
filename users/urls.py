from django.urls import path
from .views import (
    UserListView,ProviderListView,CustomerListView
)
urlpatterns = [
    path("users/",UserListView.as_view(),name="userlistview"),
    path("providers/",ProviderListView.as_view(),name="providerListview"),
    path("customers/",CustomerListView.as_view(),name="customerlistview"),
]
