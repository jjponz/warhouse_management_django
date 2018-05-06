class WarehouseItem:
    def __init__(self, name, quantity):
        self.__name = name
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    @property
    def quantity(self):
        return self.__quantity

    def discount_quantity(self):
        self.__quantity = self.__quantity - 1
