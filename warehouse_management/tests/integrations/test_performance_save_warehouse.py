from django.test import TestCase
from warehouse_management.models import WarehouseMapper, WarehouseItemMapper
from warehouse_management.django_infrastructure import DjangoWarehouseRepository
from warehouse_management.django_infrastructure import DjangoSaveWarehouseExecutor
from warehouse_management.business_logic.models.warehouses.warehouse import WarehouseItem
from warehouse_management.tests.business_logic.models.warehouses.warehouse_builder import WarehouseBuilder


class TestPerformanceSaveWarehouse(TestCase):
    def test_save_performance(self):
        warehouse = WarehouseBuilder().with_id().with_generated_items(
            1500).build()
        django_warehouse_repository = DjangoWarehouseRepository()

        django_warehouse_repository.save(warehouse)
        django_warehouse_repository.save(warehouse)

        self.assertIsNotNone(warehouse.uid)
