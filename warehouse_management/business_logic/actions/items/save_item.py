from warehouse_management.business_logic.models.actions.action_result import ActionResult
from warehouse_management.business_logic.models.items.item_validator import ItemValidator
from warehouse_management.business_logic.models.common.save_model import SaveModel
from warehouse_management.business_logic.models.validations.unicity_error import UnicityError

class SaveItem:
    def __init__ (self, item_repository):
        self.__item_repository = item_repository

    def do (self, item):
        if self.__item_repository.exists_name(item.name):
            unicity_error = UnicityError("Nombre", "Ya existe un item con ese nombre.")
            return ActionResult.create_with_errors([unicity_error])

        item_validator = ItemValidator()

        if item_validator.validate (item) is False:
            return ActionResult.create_with_errors(item_validator.errors)

        self.__save(item)

        return ActionResult()

    def __save(self, item):
        save_model = SaveModel(self.__item_repository)
        save_model.save (item)
