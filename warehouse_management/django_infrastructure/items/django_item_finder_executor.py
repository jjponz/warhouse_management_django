from warehouse_management.django_infrastructure.items.django_item_adapter import DjangoItemAdapter
from warehouse_management.django_infrastructure import DjangoItemRepository
from warehouse_management.business_logic.actions import ItemFinder

class DjangoItemFinderExecutor:
    def __init__(self, form):
        self.__form = form
        self.__adapter = DjangoItemAdapter()
        self.__action = ItemFinder(DjangoItemRepository())

    def do(self):
        property = self.__form.data['property']
        value = self.__form.data['value']

        return self.__action.do(property, value)
