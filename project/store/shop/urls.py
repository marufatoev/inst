from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('delete_cart_item/<int:pk>', views.delete_cart_item, name='delete_cart_item'),
    path('edit_cart_items/<int:pk>', views.edit_cart_items, name='edit_cart_items'),

]