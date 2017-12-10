from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.items_list, name='items_list'),
]
