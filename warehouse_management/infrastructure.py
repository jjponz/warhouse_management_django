from warehouse_management.business_logic.models.items.item import Item
from warehouse_management.models import ItemMapper
from warehouse_management.business_logic import UIDGenerator

class DjangoItemAdapter:
    def __init__(self):
        pass

    def to_item(self, django_item):
        result = Item()
        result.name = django_item.name
        result.notes = django_item.notes
        return result

    def to_django_item(self, item):
        result = ItemMapper()
        result.uid = item.uid
        result.name = item.name
        result.notes = item.notes

        return result

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
