from warehouse_management.models import UIDGenerator

class GenericModelMemoryRepository:
    def __init__ (self, model):
        self.__is_called = False
        self.__model = model
        self.__last_id_generated = None

    @classmethod
    def without_initial_model (cls):
        return cls(False)

    def save(self, model):
        self.__model = model
        self.__is_called = True

    def generate_uuid(self):
        self.__last_id_generated = UIDGenerator.generate()
        return self.__last_id_generated

    def is_called_for_save_with (self, model):
        return self.__is_called and self.__is_the_same_model (model)

    @property
    def last_id_generated(self):
        return self.__last_id_generated

    def __is_the_same_model (self, model):
        return self.__model.name == model.name

