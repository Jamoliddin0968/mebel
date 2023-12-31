from django.urls import path, include
from apps.scheduled_loans.views import ScheduledLoanViewset

from rest_framework import routers

router = routers.DefaultRouter()
router.register("", ScheduledLoanViewset)


urlpatterns = [
    path("", include(router.urls), name="Scheduled_Loan"),
]
