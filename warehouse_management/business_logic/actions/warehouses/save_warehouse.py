from warehouse_management.business_logic.models.actions.action_result import ActionResult
from warehouse_management.business_logic.models.warehouses.warehouse_validator import WarehouseValidator
from warehouse_management.business_logic.models.common.save_model import SaveModel


class SaveWarehouse:
    def __init__(self, warehouse_memory_repository):
        self.__warehouse_memory_repository = warehouse_memory_repository

    def do(self, warehouse):
        if self.__is_valid(warehouse) is False:
            return self.__build_validation_errors(warehouse)

        self.__save(warehouse)

        return ActionResult()

    def __is_valid(self, warehouse):
        self.__warehouse_validator = WarehouseValidator()
        return self.__warehouse_validator.validate(warehouse)

    def __build_validation_errors(self, warehouse):
        return ActionResult.create_with_errors(
            self.__warehouse_validator.errors)

    def __save(self, warehouse):
        save_model = SaveModel(self.__warehouse_memory_repository)
        save_model.save(warehouse)
