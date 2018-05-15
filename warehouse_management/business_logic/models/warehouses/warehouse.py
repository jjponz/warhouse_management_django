from warehouse_management.business_logic.models.warehouses.warehouse_item import WarehouseItem


class Warehouse():
    def __init__(self):
        self.__uid = None
        self.__name = ""
        self._items = []

    @classmethod
    def create(cls, uid, name, items):
        result = cls()
        result.__uid = uid
        result.__name = name
        for item in items:
            result._items.append(item)

        return result

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
        return tuple(self._items)

    @property
    def items_count(self):
        return len(self._items)

    def set_uid(self, value):
        self.__uid = value

    def has_uid(self):
        return self.__uid is not None

    def add_item(self, item_name):
        existing_item = self.__find_item(item_name)
        if not existing_item:
            self._items.append(WarehouseItem(item_name, 1))
            return

        existing_item.add_quantity()

    def discount_quantity(self, item_name):
        item_to_discount = self.__find_item(item_name)

        item_to_discount.discount_quantity()

    def contains(self, item_name):
        item = self.__find_item(item_name)

        return item is not None

    def item_quantity(self, item_name):
        item = self.__find_item(item_name)
        return item.quantity

    def __find_item(self, item_name):
        result = list(filter(lambda item: item.name == item_name, self._items))

        if not result:
            return None

        return result[0]
