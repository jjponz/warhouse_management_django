class GenericModelMemoryRepository:
    def __init__ (self, model):
        self.__is_called = False
        self.__model = model

    def save(self, model):
        self.__model = model
        self.__is_called = True

    def is_called_for_save_with (self, model):
        return self.__is_called and self.__is_the_same_model (model)

    def __is_the_same_model (self, model):
        return self.__model.property == model.property

