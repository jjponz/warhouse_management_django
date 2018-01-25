from warehouse_management.business_logic.models import Item
from warehouse_management.business_logic import UIDGenerator
from faker import Faker

class ItemBuilder():
    def __init__ (self):
        self.__item = self.__build_item()

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

    def build_random(self, number):
        return self.__build_items(number)

    def __build_items(self, number):
        result = []
        for item in range(1,number):
            result.append(self.__build_item())

        return result

    def __build_item(self):
        result = Item()
        faker = Faker()
        result.name = faker.name()
        result.notes = faker.text()

        return result



