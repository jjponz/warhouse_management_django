from warehouse_management.serializers import WarehouseSerializer
from warehouse_management.django_infrastructure import DjangoWarehouseRepository
from warehouse_management.business_logic.actions import SaveWarehouse
from warehouse_management.business_logic.models.warehouses.warehouse import Warehouse


class DjangoSaveWarehouseExecutor:
    def __init__(self, data):
        self.__data = data
        self.__action = SaveWarehouse(DjangoWarehouseRepository())

    def do(self):
        warehouse_serializer = WarehouseSerializer(data=self.__data)
        warehouse = warehouse_serializer.to_domain_object()
        print("En el do")
        print(len(warehouse.items))

        return self.__action.do(warehouse)
