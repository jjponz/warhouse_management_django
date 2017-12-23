from warehouse_management.business_logic.models.items.item import Item
from warehouse_management.models import ItemMapper
from warehouse_management.business_logic import UIDGenerator
from warehouse_management.django_infrastructure import DjangoItemAdapter

class DjangoItemRepository:
    def __init__(self):
        pass

    def exists_item_with_name(self, name):
        return ItemMapper.objects.filter(name=name)

    def generate_uid(self):
        return UIDGenerator.generate()

    def save(self, item):
        adapter = DjangoItemAdapter()
        django_item = adapter.to_django_item(item)
        django_item.save()
