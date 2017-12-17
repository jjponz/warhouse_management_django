from datetime import date

class FreezeTimeProvider:
    def __init__ (self, date):
        self.__date = date

    @property
    def today(self):
        return self.__date
