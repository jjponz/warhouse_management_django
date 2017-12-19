from warehouse_management.business_logic.models import Item

class ItemBuilder():
    def __init__ (self):
        self.__item = Item()
        self.__item.name = "Name"

    def with_uid(self, uid):
        self.__item.set_uid(uid)

        return self

    def without_name(self):
        self.__item.name = ""

        return self

    def build(self):
        return self.__item
