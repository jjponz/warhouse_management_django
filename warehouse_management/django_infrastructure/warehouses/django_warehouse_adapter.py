from warehouse_management.business_logic.models.warehouses.warehouse import Warehouse, WarehouseItem
from warehouse_management.models import WarehouseMapper, WarehouseItemMapper


class DjangoWarehouseAdapter:
    def __init__(self):
        pass

    def to_warehouse(self, django_warehouse):
        return Warehouse.create(django_warehouse.uid, django_warehouse.name,
                                self.__build_warehouse_items(django_warehouse))

    def to_django_warehouse(self, warehouse):
        result = WarehouseMapper()
        result.uid = warehouse.uid
        result.name = warehouse.name
        self.__add_warehouse_items_mapper(result, warehouse.items)

        return result

    def __build_warehouse_items(self, django_warehouse):
        result = []
        for item in django_warehouse.items.all():
            result.append(WarehouseItem(item.name, item.quantity))

        return result

    def __add_warehouse_items_mapper(self, django_warehouse, items):
        for item in items:
            warehouse_item = WarehouseItemMapper()
            warehouse_item.name = item.name
            warehouse_item.quantity = item.quantity
            print("Esto imprime algo??? " + warehouse_item.name)
            WarehouseMapper.save(django_warehouse)
            WarehouseItemMapper.save(warehouse_item)
            print("Ya lo he salvado")
            django_warehouse.items.add(warehouse_item)
