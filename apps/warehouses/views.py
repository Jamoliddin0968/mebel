from rest_framework import viewsets
from .models import WareHouse

from .serializers import WareHouseSerializer


class WareHouseViewSet(viewsets.ModelViewSet):
    serializer_class = WareHouseSerializer
    queryset = WareHouse.objects.all()

    http_method_names = ['get', 'post', 'put', 'delete',]
