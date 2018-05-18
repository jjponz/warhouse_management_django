from django.contrib import admin
from .models import ItemMapper, WarehouseMapper

admin.site.register(ItemMapper)
admin.site.register(WarehouseMapper)
