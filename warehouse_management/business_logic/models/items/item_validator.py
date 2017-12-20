from warehouse_management.business_logic.models.validations.validation_error import ValidationError

class ItemValidator:
    def __init__(self):
        self.__errors = []

    def validate(self, item):
        if item.name is "":
            self.__add_error (ValidationError("Nombre", "El nombre del item es requerido"))

        return len(self.__errors) == 0

    @property
    def errors(self):
        return self.__errors

    def __add_error(self, error):
        self.__errors.append(error)
