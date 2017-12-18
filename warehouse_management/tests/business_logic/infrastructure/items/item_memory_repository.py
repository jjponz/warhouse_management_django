from warehouse_management.business_logic import UIDGenerator

class ItemMemoryRepository:
    def __init__(self):
        self.__last_id_generated = None

    def last_id_generated(self):
        return self.__last_id_generated

    def generate_uid(self):
        self.__last_id_generated = UIDGenerator.generate()
        return self.__last_id_generated

    def save(self, model):
        self.__model = model

