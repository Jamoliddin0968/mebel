from django.contrib import admin

from product.models import (Product,Stock,SuiteItems)

admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(SuiteItems)

