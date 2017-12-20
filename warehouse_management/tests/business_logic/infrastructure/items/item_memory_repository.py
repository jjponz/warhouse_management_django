from warehouse_management.business_logic import UIDGenerator

class ItemMemoryRepository:
    def __init__(self):
        self.__last_id_generated = ""
        self.__item = None

    def last_id_generated(self):
        return self.__last_id_generated

    def generate_uid(self):
        self.__last_id_generated = UIDGenerator.generate()
        return self.__last_id_generated

    def save(self, item):
        self.__item = item

    def get(self, item_uid):
        return self.__item

    def exists_item_with_name(self, item_name):
        if self.__item is None:
            return False

        return item_name == self.__item.name

