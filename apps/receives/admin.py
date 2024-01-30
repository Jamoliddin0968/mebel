from django.contrib import admin

# Register your models here.
from .models import Receive,ReceiveItem

admin.site.register([Receive,ReceiveItem])