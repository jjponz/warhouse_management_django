from django.test import TestCase
from warehouse_management.business_logic.models.warehouses.warehouse import Warehouse
from warehouse_management.business_logic.actions.warehouses.save_warehouse import SaveWarehouse
from warehouse_management.tests.business_logic.infrastructure.warehouses.warehouse_memory_repository import WarehouseMemoryRepository
from warehouse_management.tests.business_logic.models.items.item_builder import ItemBuilder
from warehouse_management.tests.business_logic.models.warehouses.warehouse_builder import WarehouseBuilder
import mock


class TestSaveWarehouseShould(TestCase):
    def test_return_action_result_with_errors_if_warehouse_has_not_name(self):
        warehouse_builder = WarehouseBuilder()
        warehouse = warehouse_builder.without_name().build()
        warehouse_memory_repository = mock.Mock()
        save_warehouse = SaveWarehouse(warehouse_memory_repository)

        action_result = save_warehouse.do(warehouse)

        self.assertTrue(action_result.has_errors())
        self.assertEqual("Nombre", action_result.errors[0].property_name)
        self.assertEqual("El nombre del almacén es requerido",
                         action_result.errors[0].message_error)

    def test_save_warehouse_if_have_not_errors(self):
        warehouse_builder = WarehouseBuilder()
        warehouse = warehouse_builder.build()
        warehouse_memory_repository = mock.Mock()
        save_warehouse = SaveWarehouse(warehouse_memory_repository)

        save_warehouse.do(warehouse)

        warehouse_memory_repository.save.assert_called_with(warehouse)

    def test_return_action_result_with_errors_if_warehouse_has_bad_warehouse_item(
            self):
        warehouse_builder = WarehouseBuilder()
        warehouse_memory_repository = mock.Mock()
        save_warehouse = SaveWarehouse(warehouse_memory_repository)
        item = ItemBuilder().build()
        warehouse = warehouse_builder.add_item_with_negative_quantity(
            item).build()

        action_result = save_warehouse.do(warehouse)

        self.assertTrue(action_result.has_errors())
        self.assertEqual("Item", action_result.errors[0].property_name)
        self.assertEqual(
            "Un almacén no puede tener items con cantidades negativas",
            action_result.errors[0].message_error)

    def test_return_action_result_with_errors_if_warehouse_has_repeated_warehouse_items(
            self):
        warehouse_builder = WarehouseBuilder()
        warehouse_memory_repository = mock.Mock()
        save_warehouse = SaveWarehouse(warehouse_memory_repository)
        item = ItemBuilder().with_name("name").build()
        warehouse = warehouse_builder.add_item(item).add_item(item).build()

        action_result = save_warehouse.do(warehouse)

        self.assertTrue(action_result.has_errors())
        self.assertEqual("Item", action_result.errors[0].property_name)
        self.assertEqual("Un almacén no puede tener items repetidos",
                         action_result.errors[0].message_error)

    def test_save_warehouse_if_have_all_items_with_possitive_quantities(self):
        warehouse_builder = WarehouseBuilder()
        warehouse_memory_repository = mock.Mock()
        save_warehouse = SaveWarehouse(warehouse_memory_repository)
        item = ItemBuilder().with_name("name").build()
        warehouse = warehouse_builder.add_item(item).build()

        save_warehouse.do(warehouse)

        warehouse_memory_repository.save.assert_called_with(warehouse)
