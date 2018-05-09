from warehouse_management.business_logic.models.actions.action_result import ActionResult
from warehouse_management.business_logic.models.validations.validation_error import ValidationError


class WarehouseItemAdder:
    def __init__(self, warehouse_repository):
        self.__warehouse_repository = warehouse_repository

    def do(self, warehouse_uid, item_name):
        warehouse = self.__warehouse_repository.get(warehouse_uid)
        if not self.__validate_warehouse(warehouse):
            return self.__warehouse_not_exists()

        warehouse.add_item(item_name)
        self.__warehouse_repository.save(warehouse)

        return ActionResult()

    def __validate_warehouse(self, warehouse):
        return warehouse is not None

    def __warehouse_not_exists(self):
        return ActionResult.create_with_errors(
            [ValidationError("Almacén", "El almacén no existe")])
