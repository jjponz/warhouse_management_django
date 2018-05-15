from django.test import TestCase
from warehouse_management.models import WarehouseMapper, WarehouseItemMapper
from warehouse_management.django_infrastructure import DjangoWarehouseRepository
from warehouse_management.django_infrastructure import DjangoSaveWarehouseExecutor
from warehouse_management.business_logic.models.warehouses.warehouse import WarehouseItem
from warehouse_management.tests.business_logic.models.warehouses.warehouse_builder import WarehouseBuilder


class TestDjangoSaveWarehouseExecutorShould(TestCase):
    def test_save_warehouse_if_warehouse_is_valid(self):
        data = {
            'uid': 'SomeUid',
            'name': 'SomeWarehouse',
            'warehouse_items': [{
                'name': 'Item1',
                'quantity': '2'
            }]
        }
        django_save_warehouse_executor = DjangoSaveWarehouseExecutor(data)

        action_result = django_save_warehouse_executor.do()

        django_warehouse_repository = DjangoWarehouseRepository()
        warehouse = django_warehouse_repository.get('SomeUid')
        self.assertFalse(action_result.has_errors())
        self.assertEqual('SomeWarehouse', warehouse.name)
        self.assertEqual(1, warehouse.items_count)

    def test_save_wareohouse_with_multiples_items(self):
        data = {
            'uid':
            'Some_uid',
            'name':
            'SomeWarehouse',
            'warehouse_items': [{
                'name': 'Item2',
                'quantity': 5
            }, {
                'name': 'Item22',
                'quantity': 5
            }, {
                'name': 'Item222',
                'quantity': 3
            }]
        }
        django_save_warehouse_executor = DjangoSaveWarehouseExecutor(data)

        django_save_warehouse_executor.do()

        django_warehouse_repository = DjangoWarehouseRepository()
        warehouse = django_warehouse_repository.get('Some_uid')
        expected_warehouse_items = self.__buildExpectedWarehouseItems()
        for item in expected_warehouse_items:
            self.assertTrue(warehouse.contains(item.name))

    def test_not_save_warehouse_with_repeated_items(self):
        data = {
            'name':
            'SomeWarehouse',
            'warehouse_items': [{
                'name': 'Item2',
                'quantity': 5
            }, {
                'name': 'Item2',
                'quantity': 5
            }, {
                'name': 'Item222',
                'quantity': 3
            }]
        }

        django_save_warehouse_executor = DjangoSaveWarehouseExecutor(data)

        django_save_warehouse_executor.do()

        django_warehouse_repository = DjangoWarehouseRepository()
        warehouse = django_warehouse_repository.get('Some_uid')
        self.assertIsNone(warehouse)

    def test_performance(self):
        warehouse = WarehouseBuilder().with_id().with_generated_items(
            3).build()
        django_warehouse_repository = DjangoWarehouseRepository()

        django_warehouse_repository.save(warehouse)

        self.assertIsNotNone(warehouse.uid)

    def __buildExpectedWarehouseItems(self):
        return [
            WarehouseItem('Item2', 5),
            WarehouseItem('Item22', 5),
            WarehouseItem('Item222', 3)
        ]
