from django.shortcuts import render

def items_list(request):
    return render(request, 'items/items_list.html')
