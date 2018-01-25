from django.test import TestCase
from warehouse_management.forms import ItemFinderForm
from warehouse_management.tests.business_logic.models.items.item_builder import ItemBuilder
from warehouse_management.django_infrastructure import DjangoItemRepository
from warehouse_management.django_infrastructure import DjangoItemFinderExecutor

class TestDjangoItemFinderExecutorShould(TestCase):
    def test_find_items_by_name(self):
        self.__init_repository()
        item_form = ItemFinderForm(data={'property':'name', 'value':'Juanjo'})
        django_item_finder_executor = DjangoItemFinderExecutor (item_form)

        finded_items = django_item_finder_executor.do()

        self.assertEqual(1, len(finded_items))



    def __init_repository(self):
        self.__item_repository = DjangoItemRepository()
        item = ItemBuilder().with_name("Juanjo").with_generated_uid().build()
        self.__item_repository.save(item)
        items = ItemBuilder().build_random(3)
        self.__item_repository.add_range(items)
