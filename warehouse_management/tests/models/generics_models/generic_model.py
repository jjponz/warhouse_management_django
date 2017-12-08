class GenericModel():
    def __init__ (self):
        self.__property = ""

    @property
    def property(self):
        return self.__property

    @property.setter
    def property(self, value):
        self.__property = value
