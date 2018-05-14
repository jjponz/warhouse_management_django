from django.test import TestCase
from warehouse_management.models import WarehouseMapper, WarehouseItemMapper
from warehouse_management.django_infrastructure import DjangoWarehouseRepository
from warehouse_management.django_infrastructure import DjangoSaveWarehouseExecutor


class TestDjangoSaveWarehouseExecutorShould(TestCase):
    def test_save_warehouse_if_warehouse_is_valid(self):
        data = {
            'uid': 'Some_uid',
            'name': 'SomeWarehouse',
            'warehouse_items': [{
                'name': 'Item1',
                'quantity': '2'
            }]
        }
        django_save_warehouse_executor = DjangoSaveWarehouseExecutor(data)

        django_save_warehouse_executor.do()

        django_warehouse_repository = DjangoWarehouseRepository()
        warehouse = django_warehouse_repository.get('Some_uid')

        self.assertEqual('SomeWarehouse', warehouse.name)
        self.assertEqual(1, warehouse.items_count)

        data = {
            'uid':
            'Some_uid',
            'name':
            'SomeWarehouse',
            'warehouse_items': [{
                'name': 'Item2',
                'quantity': '5'
            }, {
                'name': 'Item22',
                'quantity': '5'
            }, {
                'name': 'Item222',
                'quantity': '3'
            }]
        }

        django_save_warehouse_executor = DjangoSaveWarehouseExecutor(data)

        django_save_warehouse_executor.do()

        django_warehouse_repository = DjangoWarehouseRepository()
        warehouse = django_warehouse_repository.get('Some_uid')

        for item in WarehouseItemMapper.objects.all():
            print(item.name)

        print("Final del test, cuantos objectos hay??")
        print(WarehouseItemMapper.objects.all().count())
        self.assertEqual('SomeWarehouse', warehouse.name)
        self.assertEqual(3, warehouse.items_count)
