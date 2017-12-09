from django.test import TestCase
from warehouse_management.actions import CreateModel
from warehouse_management.tests.models.generics_models.generic_model import GenericModel
from warehouse_management.tests.infrastructure.generic_model_repository import GenericModelMemoryRepository

class CreateModelShould(TestCase):
    def test_assign_id(self):
        model_repository = GenericModelMemoryRepository.without_initial_model()
        model = GenericModel ()
        create_model = CreateModel(model_repository)

        create_model.do(model)

        self.assertEqual(model_repository.last_id_generated, model.uuid)
