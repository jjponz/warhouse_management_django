class ValidationError:
    def __init__(self, property_name, message):
        self.__property_name = property_name
        self.__message = message

    @property
    def property_name(self):
        return self.__property_name

    @property
    def message_error(self):
        return self.__message
