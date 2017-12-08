class CreateModel():

    def __init__ (self, item_repository):
        self._item_repository = item_repository

    def do(self, item):
        self._item_repository.save(item)

