from warehouse_management.business_logic.models.actions.action_result import ActionResult
from warehouse_management.business_logic.models.items.item_validator import ItemValidator
from warehouse_management.business_logic.models.common.save_model import SaveModel
from warehouse_management.business_logic.models.validations.unicity_error import UnicityError

class SaveItem:
    def __init__ (self, item_repository):
        self.__item_repository = item_repository

    def do (self, item):
        if item.uid is None and self.__item_repository.exists_item_with_name(item.name):
           return self.__build_unicity_error()

        if self.__is_valid(item) is False:
            return self.__build_validation_errors(item)

        self.__save(item)

        return ActionResult()

    def __build_unicity_error(self):
            unicity_error = UnicityError("Nombre", "Ya existe un item con ese nombre.")
            return ActionResult.create_with_errors([unicity_error])

    def __is_valid(self, item):
        self.__item_validator = ItemValidator()
        return self.__item_validator.validate(item)

    def __build_validation_errors(self, item):
        return ActionResult.create_with_errors(self.__item_validator.errors)

    def __save(self, item):
        save_model = SaveModel(self.__item_repository)
        save_model.save (item)
