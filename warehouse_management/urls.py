from django.urls import path
from . import views

urlpatterns = [
    path(r'items/list', views.items_list, name='items_list'),
]
