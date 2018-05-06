from warehouse_management.business_logic.models.warehouses.warehouse_item import WarehouseItem


class Warehouse():
    def __init__(self):
        self.__uid = None
        self.__name = ""
        self.__items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def uid(self):
        return self.__uid

    @property
    def items(self):
        return tuple(self.__items)

    def set_uid(self, value):
        self.__uid = value

    def has_uid(self):
        return self.__uid is not None

    def add_item(self, item):
        self.__items.append(WarehouseItem(item.name, 1))

    def discount_quantity(self, item):
        item_to_discount = list(
            filter(lambda _item: _item.name == item.name, self.__items))

        item_to_discount[0].discount_quantity()
