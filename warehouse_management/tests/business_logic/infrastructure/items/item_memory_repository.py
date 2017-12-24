from warehouse_management.business_logic import UIDGenerator

class ItemMemoryRepository:
    def __init__(self):
        self.__last_id_generated = ""
        self.__items = []

    def last_id_generated(self):
        return self.__last_id_generated

    def generate_uid(self):
        self.__last_id_generated = UIDGenerator.generate()
        return self.__last_id_generated

    def save(self, item):
        self.__items.append(item)

    def save_list (self, items):
        for item in items:
            self.save(item)

    def get(self, item_uid):
        return next((item for item in self.__items if item.uid == item_uid), None)

    def exists_item_with_name(self, item_name):
        result = next((item for item in self.__items if item.name == item_name), None)

        return result != None

    def count(self):
        return len(self.__items)

    def get_by(self, property, value_to_find):
        return [item for item in self.__items if value_to_find in getattr(item, property)]
