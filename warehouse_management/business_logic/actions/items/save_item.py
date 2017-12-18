from warehouse_management.business_logic.models.actions.action_result import ActionResult

class SaveItem:
    def __init__ (self, item_repository):
        self.__item_repository = item_repository

    def do (self, item):
        return ActionResult()
