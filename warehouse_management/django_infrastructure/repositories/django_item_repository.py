from warehouse_management.models import ItemMapper
from warehouse_management.business_logic import UIDGenerator
from warehouse_management.django_infrastructure.items.django_item_adapter import DjangoItemAdapter


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

    def add_range(self, items):
        for item in items:
            self.save(item)

    def count(self):
        return ItemMapper.objects.all().count()

    def get_by(self, property, value):
        filter_to_apply = {
            "{}__icontains".format(property) : value,
        }

        return ItemMapper.objects.filter(**filter_to_apply)
