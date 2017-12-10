from django.test import TestCase
from datetime import date
from warehouse_management.actions import CreateModel
from warehouse_management.tests.models.generics_models.generic_model import GenericModel
from warehouse_management.tests.infrastructure.generic_model_repository import GenericModelMemoryRepository
from warehouse_management.tests.infrastructure.freeze_time_provider import FreezeTimeProvider

class CreateModelShould(TestCase):
    def test_assign_id(self):
        model_repository = GenericModelMemoryRepository.without_initial_model()
        model = GenericModel ()
        create_model = CreateModel(model_repository)

        create_model.do(model)

        self.assertEqual(model_repository.last_id_generated, model.uuid)

    def test_assign_creation_date(self):
        time_provider = FreezeTimeProvider(date(2001, 1, 1))
        model_repository = GenericModelMemoryRepository.without_initial_model()
        model = GenericModel ()
        create_model = CreateModel(model_repository)
        create_model.set_time_provider(time_provider)

        create_model.do(model)

        self.assertEqual(model.creation_date, time_provider.today)
