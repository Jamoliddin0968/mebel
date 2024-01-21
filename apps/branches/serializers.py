from rest_framework.serializers import CharField, ModelSerializer

from apps.products.models import Product
from apps.warehouse_items.models import WareHouseItem
from apps.warehouses.models import WareHouse

from .models import Branch


class BranchSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"

    def create(self, validated_data):
        new_branch = super().create(validated_data)
        new_ware, b = WareHouse.objects.get_or_create(branch=new_branch)

        products = Product.objects.all()

        for product in products:
            c, n = WareHouseItem.objects.get_or_create(
                warehouse=new_ware, product=product)
        return new_branch
