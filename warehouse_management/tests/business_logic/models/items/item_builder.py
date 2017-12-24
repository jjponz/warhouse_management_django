from warehouse_management.business_logic.models import Item
from warehouse_management.business_logic import UIDGenerator

class ItemBuilder():
    def __init__ (self):
        self.__item = Item()
        self.__item.name = "Name"

    def with_uid(self, uid):
        self.__item.set_uid(uid)

        return self

    def with_name(self, name):
        self.__item.name = name

        return self

    def with_notes(self, notes):
        self.__item.notes = notes

        return self

    def with_generated_uid(self):
        self.__item.set_uid(UIDGenerator().generate())

        return self

    def without_name(self):
        self.__item.name = ""

        return self

    def build(self):
        return self.__item
