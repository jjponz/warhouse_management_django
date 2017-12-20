class SaveModel():
    def __init__(self, model_repository):
        self.__model_repository = model_repository

    def save(self, model):
        if not model.has_uid():
            model.set_uid (self.__model_repository.generate_uid())

        self.__model_repository.save(model)
