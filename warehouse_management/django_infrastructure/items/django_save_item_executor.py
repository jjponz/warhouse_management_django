from warehouse_management.django_infrastructure.items.django_item_adapter import DjangoItemAdapter
from warehouse_management.django_infrastructure import DjangoItemRepository
from warehouse_management.business_logic.actions import SaveItem

class DjangoSaveItemExecutor:
    def __init__(self, form):
        self.__form = form
        self.__adapter = DjangoItemAdapter()
        self.__action = SaveItem(DjangoItemRepository())

    def do (self):
        django_item = self.__form.save(commit=False)
        item = self.__adapter.to_item(django_item)

        return self.__action.do(item)


