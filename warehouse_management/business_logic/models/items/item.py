class Item:
    def __init__(self):
        self.__uuid = None

    @property
    def uuid(self):
        return self.__uuid


    def set_uid(self, value):
        self.__uuid = value
