from django.test import TestCase
from warehouse_management.models import Item
from warehouse_management.actions import CreateModel
from warehouse_management.infrastructure.items.item_django_repository import ItemDjangoRepository


class CreateModelShould(TestCase):
    def test_assign_id_if_is_new_model(self):
        item = Item()
        item_repository = ItemDjangoRepository ()
        create_item = CreateModel(item_repository)

        create_item.do(item)

        self.assertEqual(1, item.id)
