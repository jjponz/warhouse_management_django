from django.test import TestCase
from warehouse_management.business_logic.actions import SaveItem
from warehouse_management.tests.business_logic.models.items.item_builder import ItemBuilder
from warehouse_management.tests.business_logic.infrastructure.items.item_memory_repository import ItemMemoryRepository
# from warehouse_management.tests.business_logic.infrastructure.common.freeze_time_provider import FreezeTimeProvider

class TestSaveItemShould(TestCase):
    def test_return_action_result_without_errors_if_item_is_valid(self):
        item = ItemBuilder().build()
        item_memory_repository = ItemMemoryRepository()
        save_item = SaveItem(item_memory_repository)

        action_result = save_item.do (item)

        self.assertEqual(0, action_result.has_errors())

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
