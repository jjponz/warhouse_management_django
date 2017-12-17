class EditModel():

    def __init__(self, repository):
        self.__repository = repository

    def do(self, item):
        self.__repository.save(item)
