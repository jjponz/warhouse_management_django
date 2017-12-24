from django.test import TestCase
from warehouse_management.business_logic.actions import ItemFinder
from warehouse_management.tests.business_logic.models.items.item_builder import ItemBuilder
from warehouse_management.tests.business_logic.infrastructure.items.item_memory_repository import ItemMemoryRepository

class TestItemFinderShould(TestCase):
    def test_find_items_by_name(self):
        items = self.__build_items(50)
        item_memory_repository = self.__init_repository_with(items)
        item_finder = ItemFinder(item_memory_repository)

        finded_items = item_finder.find("name", "Mesa")

        self.assertEqual(1, len(finded_items))

    def test_find_items_by_notes(self):
        items = self.__build_items(50)
        item_memory_repository = self.__init_repository_with(items)
        item_finder = ItemFinder(item_memory_repository)

        finded_items = item_finder.find("notes", "Negra")

        self.assertEqual(1, len(finded_items))

    def __build_items(self, number_of_items):
        items = [ ItemBuilder().with_name("Mesa").with_notes("Negra y grande").with_generated_uid().build()]

        for _ in range(49):
            items.append(ItemBuilder().with_generated_uid().build())

        return items

    def __init_repository_with(self, items):
        result = ItemMemoryRepository()
        result.save_list(items)

        return result

