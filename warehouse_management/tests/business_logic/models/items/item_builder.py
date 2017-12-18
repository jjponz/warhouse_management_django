from warehouse_management.business_logic.models import Item

class ItemBuilder():
    def __init__ (self):
        self.__item = Item()

    def with_uid(self, uid):
        self.__item.set_uid(uid)

        return self

    def build(self):
        return self.__item
