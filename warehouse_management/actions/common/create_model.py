from warehouse_management.infrastructure.common.default_time_provider import DefaultTimeProvider

class CreateModel():

    def __init__ (self, model_repository):
        self.__model_repository= model_repository
        self.__time_provider = DefaultTimeProvider()

    def do(self, item):
        item.set_uid(self.__model_repository.generate_uuid());
        item.creation_date = self.__time_provider.today
        self.__model_repository.save(item)

    def set_time_provider (self, time_provider):
        self.__time_provider = time_provider

