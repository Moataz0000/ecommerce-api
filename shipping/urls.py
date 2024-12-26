from django.urls import path
from . import views


app_name = 'shipping'



urlpatterns = [
    path('cart/', views.CartDetailView.as_view(), name='cart-detail'),
    path('cart/add/', views.CartItemAddView.as_view(), name='cart-item-add'),
    path('cart/update/<int:pk>/', views.CartItemUpdateView.as_view(), name='cart-item-update'),
    path('cart/delete/<int:pk>/', views.CartItemDeleteView.as_view(), name='cart-item-delete'),
]