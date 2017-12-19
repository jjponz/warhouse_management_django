from warehouse_management.business_logic.models.actions.action_result import ActionResult
from warehouse_management.business_logic.models.items.item_validator import ItemValidator

class SaveItem:
    def __init__ (self, item_repository):
        self.__item_repository = item_repository

    def do (self, item):
        item_validator = ItemValidator()

        if item_validator.validate (item) is False:
            return ActionResult.add_errors(item_validator.errors)

        if not item.has_uid():
            item.set_uid (self.__item_repository.generate_uid())

        self.__item_repository.save(item)

        return ActionResult()
