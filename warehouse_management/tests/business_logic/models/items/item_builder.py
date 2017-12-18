from warehouse_management.business_logic.models import Item

class ItemBuilder():
    def __init__ (self):
        self.__item = Item()

    def build(self):
        return self.__item
