class ActionResult:
    @classmethod
    def create_with_errors(cls, errors):
        result = cls()
        result.__add_errors(errors)
        return result

    def __init__(self):
        self.__errors = []

    def has_errors(self):
        return len(self.__errors) > 0

    @property
    def errors(self):
        return self.__errors

    def __add_errors(self, errors):
        self.__errors.extend(errors)


