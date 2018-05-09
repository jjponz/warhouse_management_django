from django.test import TestCase
from warehouse_management.business_logic.models.warehouses.warehouse import Warehouse
from warehouse_management.business_logic.actions.warehouses.warehouse_item_adder import WarehouseItemAdder
from warehouse_management.tests.business_logic.infrastructure.warehouses.warehouse_memory_repository import WarehouseMemoryRepository
from warehouse_management.tests.business_logic.models.items.item_builder import ItemBuilder
from warehouse_management.tests.business_logic.models.warehouses.warehouse_builder import WarehouseBuilder
import mock


class TestWarehouseItemAdder(TestCase):
    def test_add_item_to_warehouse(self):
        warehouse = WarehouseBuilder().with_id().build()
        item = ItemBuilder().build()
        warehouse_memory_repository = mock.Mock()
        warehouse_memory_repository.get.return_value = warehouse
        warehouse_item_adder = WarehouseItemAdder(warehouse_memory_repository)

        warehouse_item_adder.do(warehouse.uid, item.name)

        self.assertTrue(warehouse.contains(item.name))

    def test_return_action_result_without_errors_when_add_item(self):
        warehouse = WarehouseBuilder().with_id().build()
        item = ItemBuilder().build()
        warehouse_memory_repository = mock.Mock()
        warehouse_memory_repository.get.return_value = warehouse
        warehouse_item_adder = WarehouseItemAdder(warehouse_memory_repository)

        action_result = warehouse_item_adder.do(warehouse.uid, item.name)

        self.assertFalse(action_result.has_errors())

    def test_return_action_result_with_errors_if_not_exists_warehouse(self):
        item = ItemBuilder().build()
        warehouse_memory_repository = mock.Mock()
        warehouse_memory_repository.get.return_value = None
        warehouse_item_adder = WarehouseItemAdder(warehouse_memory_repository)

        action_result = warehouse_item_adder.do("some_non_existing_id",
                                                item.name)

        self.assertTrue(action_result.has_errors())

    def test_sum_one_to_quantity_if_item_already_exists(self):
        item = ItemBuilder().build()
        warehouse = WarehouseBuilder().with_id().add_item(item.name).build()
        warehouse_memory_repository = mock.Mock()
        warehouse_memory_repository.get.return_value = warehouse
        warehouse_item_adder = WarehouseItemAdder(warehouse_memory_repository)

        warehouse_item_adder.do(warehouse.uid, item.name)

        self.assertEqual(2, warehouse.item_quantity(item.name))
