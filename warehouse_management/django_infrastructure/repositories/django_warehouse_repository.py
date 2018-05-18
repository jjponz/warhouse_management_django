from warehouse_management.models import WarehouseMapper, WarehouseItemMapper
from warehouse_management.business_logic import UIDGenerator
from warehouse_management.django_infrastructure.warehouses.django_warehouse_adapter import DjangoWarehouseAdapter
from django.core.exceptions import ObjectDoesNotExist


class DjangoWarehouseRepository:
    def __init__(self):
        self.__last_generated_uid = ""

    def generate_uid(self):
        self.__last_generated_uid = UIDGenerator.generate()
        return self.__last_generated_uid

    def get(self, uid):
        try:
            warehouse = WarehouseMapper.objects.get(uid=uid)
        except ObjectDoesNotExist:
            return None

        adapter = DjangoWarehouseAdapter()
        return adapter.to_warehouse(warehouse)

    def save(self, warehouse):
        django_warehouse = self.__to_django_warehouse(warehouse)
        django_warehouse.save()

    def exists_warehouse_with_name(self, name):
        return WarehouseMapper.objects.filter(name=name)

    def count(self):
        return WarehouseMapper.objects.all().count()

    def __to_django_warehouse(self, warehouse):
        result = WarehouseMapper()
        result.uid = warehouse.uid
        result.name = warehouse.name
        result.save()
        result.items.all().delete()
        self.__add_warehouse_items_mapper(result, warehouse.items)

        return result

    def __add_warehouse_items_mapper(self, django_warehouse, items):
        for item in items:
            warehouse_item = WarehouseItemMapper()
            warehouse_item.name = item.name
            warehouse_item.quantity = item.quantity
            WarehouseItemMapper.save(warehouse_item)
            django_warehouse.items.add(warehouse_item)
