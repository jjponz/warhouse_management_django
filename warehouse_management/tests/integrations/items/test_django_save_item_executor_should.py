from django.test import TestCase
from warehouse_management.forms import ItemForm
from warehouse_management.models import ItemMapper
from warehouse_management.django_infrastructure import DjangoItemAdapter, DjangoItemRepository
from warehouse_management.business_logic.actions import SaveItem
from warehouse_management.business_logic import DjangoSaveItemExecutor

class TestDjangoSaveItemExecutorShould(TestCase):
    def test_save_item_if_item_is_valid(self):
        item_form = ItemForm(data={'name':'Juanjo', 'notes':'some note'})
        django_adapter = DjangoItemAdapter()
        django_item_repository = DjangoItemRepository()
        save_item = SaveItem(django_item_repository)
        django_save_item_executor = DjangoSaveItemExecutor(item_form, django_adapter, save_item)

        django_save_item_executor.do()

        self.assertTrue(django_item_repository.exists_item_with_name('Juanjo'))

    def test_not_save_item_if_item_is_not_valid(self):
        item_form = ItemForm(data={'name':'', 'notes':'some note'})
        django_adapter = DjangoItemAdapter()
        django_item_repository = DjangoItemRepository()
        save_item = SaveItem(django_item_repository)
        django_save_item_executor = DjangoSaveItemExecutor(item_form, django_adapter, save_item)

        django_save_item_executor.do()

        self.assertFalse(django_item_repository.exists_item_with_name(''))
        self.assertEqual(0, ItemMapper.objects.all().count())
