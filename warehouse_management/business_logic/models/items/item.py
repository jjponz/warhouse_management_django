class Item:
    def __init__(self):
        self.__uid = None
        self.__name = ""
        self.__notes = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value):
        self.__notes = value

    @property
    def uid(self):
        return self.__uid

    def set_uid(self, value):
        self.__uid = value

    def has_uid(self):
        return self.__uid is not None
