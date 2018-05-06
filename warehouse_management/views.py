from django.shortcuts import render
from .forms import ItemFinderForm
from warehouse_management.django_infrastructure import DjangoItemRepository
from warehouse_management.django_infrastructure import DjangoItemFinderExecutor
from warehouse_management.business_logic.models import Renderizer


def items_list(request):
    form = ItemFinderForm()
    finded_items = []
    if request.method == "POST":
        form = ItemFinderForm(request.POST)
        django_item_finder_executor = DjangoItemFinderExecutor()
        finded_items = django_item_finder_executor.do('name',
                                                      form['value'].value())

    return render(request, Renderizer.view('items_list'),
                  Renderizer.build_template_data({
                      'form': form,
                      'finded_items': finded_items
                  }))
    # return render(request, 'items/items_list.html', {'form': form, 'finded_items' : finded_items})
