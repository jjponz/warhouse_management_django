class Item:
    def __init__(self):
        self.__uid = None

    @property
    def uid(self):
        return self.__uid

    def set_uid(self, value):
        self.__uid = value

    def has_uid(self):
        return self.__uid is not None
