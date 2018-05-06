from warehouse_management.business_logic.models.validations.validation_error import ValidationError


class WarehouseValidator:
    def __init__(self):
        self.__errors = []

    def validate(self, warehouse):
        self.__validate_warehouse_name_is_not_empty(warehouse.name)
        self.__validate_warehouse_items_has_possitive_quantities(
            warehouse.items)
        return len(self.__errors) == 0

    @property
    def errors(self):
        return self.__errors

    def __add_error(self, error):
        self.__errors.append(error)

    def __validate_warehouse_name_is_not_empty(self, name):
        if name is "":
            self.__add_error(
                ValidationError("Nombre",
                                "El nombre del almacén es requerido"))

    def __validate_warehouse_items_has_possitive_quantities(self, items):
        for item in items:
            if item.quantity < 0:
                self.__add_error(
                    ValidationError(
                        "Item",
                        "Un almacén no puede tener items con cantidades negativas"
                    ))
