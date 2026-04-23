from django.urls import path
from .views import cart_view, add_to_cart, increase_quantity, decrease_quantity, remove_from_cart

urlpatterns = [
    path('', cart_view, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('increase/<int:item_id>/', increase_quantity, name='increase_quantity'),
    path('decrease/<int:item_id>/', decrease_quantity, name='decrease_quantity'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]