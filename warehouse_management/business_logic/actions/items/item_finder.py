class ItemFinder:
    def __init__(self, item_repository):
        self.__item_repository = item_repository

    def do(self, property, value_to_find):
        if value_to_find == "":
            return []

        return self.__item_repository.get_by(property, value_to_find)
