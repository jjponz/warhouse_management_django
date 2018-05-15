from rest_framework import serializers
from warehouse_management.business_logic.models.warehouses.warehouse import Warehouse, WarehouseItem


class WarehouseItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField()

    def to_domain_object(self):
        self.is_valid()
        name = self.validated_data['name']
        quantity = self.validated_data['quantity']

        return WarehouseItem(name, quantity)


class WarehouseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    uid = serializers.CharField(max_length=100, required=False)
    warehouse_items = WarehouseItemSerializer(many=True, required=False)

    def to_domain_object(self):
        self.is_valid()
        name = self.data.get('name', None)
        uid = self.data.get('uid', None)

        items = []
        for item in self.validated_data['warehouse_items']:
            items.append(WarehouseItem(item['name'], item['quantity']))

        result = Warehouse.create(uid, name, items)
        return result
