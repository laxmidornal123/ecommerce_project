from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/toggle/<int:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),
]