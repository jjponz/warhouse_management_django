from warehouse_management.business_logic.models.warehouses.warehouse import Warehouse
from warehouse_management.business_logic.models.warehouses.warehouse_item import WarehouseItem
from warehouse_management.business_logic import UIDGenerator
from faker import Faker


class WarehouseBuilder:
    def __init__(self):
        self.__warehouse = self.__build_warehouse()

    def without_name(self):
        self.__warehouse.name = ""

        return self

    def add_item(self, item_name):
        self.__warehouse._items.append(WarehouseItem(item_name, 1))

        return self

    def add_item_with_negative_quantity(self, item):
        self.__warehouse.add_item(item.name)
        self.__warehouse.discount_quantity(item.name)
        self.__warehouse.discount_quantity(item.name)

        return self

    def with_id(self):
        self.__warehouse.set_uid(UIDGenerator().generate())
        return self

    def build(self):
        return self.__warehouse

    def __build_warehouse(self):
        result = Warehouse()
        faker = Faker()
        result.name = faker.name()

        return result
