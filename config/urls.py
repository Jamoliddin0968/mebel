"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .yasg_urls import drf_yasg_urlpatterns

token_urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/products/", include("apps.products.urls")),
    path("api/v1/users/", include("apps.users.urls")),
    path('api/v1/categories/', include('apps.categories.urls')),
    path('api/v1/warehouse/', include('apps.warehouses.urls')),
    path('api/v1/warehouse-items/', include('apps.warehouse_items.urls')),
    path('api/v1/branches/', include('apps.branches.urls')),
    path('api/v1/customers/', include('apps.customers.urls')),
    path('api/v1/', include('apps.receives.urls')),
    path('api/v1/sales/', include('apps.sales.urls')),
    path('api/v1/orders/', include('apps.orders.urls')),
    path('api/v1/loans/', include('apps.loans.urls')),
    path('api/v1/notifications/', include('apps.notifications.urls')),
    path('api/v1/scheduled_loans/', include('apps.scheduled_loans.urls')),
    path('api/v1/image/', include('apps.image.urls')),
]+drf_yasg_urlpatterns+token_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
