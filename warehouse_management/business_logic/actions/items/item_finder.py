class ItemFinder:
    def __init__(self, item_repository):
        self.__item_repository = item_repository

    def find(self, property, value_to_find):
        return self.__item_repository.get_by(property, value_to_find)
