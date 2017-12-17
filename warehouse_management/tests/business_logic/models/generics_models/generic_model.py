class GenericModel():
    def __init__ (self):
        self.__name = ""
        self.__uuid = False
        self.__creation_date = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def creation_date(self):
        return self.__creation_date

    @creation_date.setter
    def creation_date(self, value):
        self.__creation_date = value

    @property
    def uuid(self):
        return self.__uuid


    def set_uid(self, value):
        self.__uuid = value

