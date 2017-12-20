from django.test import TestCase
from warehouse_management.business_logic.actions import SaveItem
from warehouse_management.tests.business_logic.models.items.item_builder import ItemBuilder
from warehouse_management.tests.business_logic.infrastructure.items.item_memory_repository import ItemMemoryRepository

class TestSaveItemShould(TestCase):
    def test_return_action_result_without_errors_if_item_is_valid(self):
        item = ItemBuilder().build()
        item_memory_repository = ItemMemoryRepository()
        save_item = SaveItem(item_memory_repository)

        action_result = save_item.do (item)

        self.assertFalse(action_result.has_errors())

    def test_return_action_result_with_errors_if_item_has_not_name(self):
        item = ItemBuilder().without_name().build()
        item_memory_repository = ItemMemoryRepository()
        save_item = SaveItem(item_memory_repository)

        action_result = save_item.do(item)

        self.assertTrue(action_result.has_errors())



    def test_return_error_that_cause_fail_action(self):
        item = ItemBuilder().without_name().build()
        item_memory_repository = ItemMemoryRepository()
        save_item = SaveItem(item_memory_repository)

        action_result = save_item.do(item)

        self.assertEqual("Nombre", action_result.errors[0].property_name)
        self.assertEqual("El nombre del item es requerido", action_result.errors[0].message_error)


    def test_assign_uid_to_item_is_item_is_new(self):
        item = ItemBuilder().build()
        item_memory_repository = ItemMemoryRepository()
        save_item = SaveItem(item_memory_repository)

        save_item.do(item)

        self.assertEqual(item_memory_repository.last_id_generated(), item.uid)

    def test_not_override_uid_to_item_if_this_already_have(self):
        uid = "uid"
        item = ItemBuilder().with_uid(uid).build()
        item_memory_repository = ItemMemoryRepository()
        save_item = SaveItem(item_memory_repository)

        save_item.do(item)

        self.assertEqual(uid, item.uid)

    def test_add_item_to_repository_if_item_is_valid(self):
        item = ItemBuilder().build()
        item_memory_repository = ItemMemoryRepository()
        save_item = SaveItem(item_memory_repository)

        save_item.do(item)

        self.assertEqual(item, item_memory_repository.get(item.uid))

    def test_not_add_item_to_repository_if_item_is_not_valid(self):
        item = ItemBuilder().without_name().build()
        item_memory_repository = ItemMemoryRepository()
        save_item = SaveItem(item_memory_repository)

        save_item.do(item)

        self.assertIsNone(item_memory_repository.get(item.uid))
