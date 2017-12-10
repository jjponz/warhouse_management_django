from django.test import TestCase
from warehouse_management.actions import EditModel
from warehouse_management.tests.models.generics_models.generic_model import GenericModel
from warehouse_management.tests.infrastructure.generic_model_repository import GenericModelMemoryRepository

class EditModelShould(TestCase):
    def test_update_model (self):
        model = GenericModel()
        model_repository = self.__init_model_repository_with (model)
        self.__update_model(model)
        edit_model = EditModel (model_repository)

        edit_model.do (model)

        self.assertTrue(model_repository.is_called_for_save_with(model))

    # private

    def __init_model_repository_with (self, model):
        result = GenericModelMemoryRepository (model)
        return result

    def __update_model (self, model):
        model.name = "new value"
