from django.urls import path
from . import views
from .views import add_item, list_items, update_item

urlpatterns = [
    path('', views.home, name='home'),
    path('add_item/', add_item, name='add_item'),
    path('list_items/', list_items, name='list_items'),
    path('update_item/<int:item_id>/', update_item, name='update_item'),
]