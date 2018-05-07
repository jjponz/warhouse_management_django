from warehouse_management.business_logic.models.warehouses.warehouse import Warehouse
from faker import Faker


class WarehouseBuilder:
    def __init__(self):
        self.__warehouse = self.__build_warehouse()

    def without_name(self):
        self.__warehouse.name = ""

        return self

    def add_item(self, item):
        self.__warehouse.add_item(item)

        return self

    def add_item_with_negative_quantity(self, item):
        self.__warehouse.add_item(item)
        self.__warehouse.discount_quantity(item)
        self.__warehouse.discount_quantity(item)

        return self

    def build(self):
        return self.__warehouse

    def __build_warehouse(self):
        result = Warehouse()
        faker = Faker()
        result.name = faker.name()

        return result
