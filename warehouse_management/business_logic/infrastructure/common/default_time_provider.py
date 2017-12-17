from datetime import date

class DefaultTimeProvider:

    @property
    def today(self):
        return date.today()
