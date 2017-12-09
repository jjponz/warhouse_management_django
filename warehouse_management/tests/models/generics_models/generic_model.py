class GenericModel():
    def __init__ (self):
        self.__name = ""
        self.__uuid = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def uuid(self):
        return self.__uuid


    def set_uid(self, value):
        self.__uuid = value


