from warehouse_management.business_logic.models.actions.action_result import ActionResult
from warehouse_management.business_logic.models.items.item_validator import ItemValidator
from warehouse_management.business_logic.models.common.save_model import SaveModel

class SaveItem:
    def __init__ (self, item_repository):
        self.__item_repository = item_repository

    def do (self, item):
        item_validator = ItemValidator()

        if not item_validator.validate (item):
            return ActionResult.create_with_errors(item_validator.errors)

        save_model = SaveModel(self.__item_repository)
        save_model.save (item)


        return ActionResult()
