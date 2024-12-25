from django.urls import path
from . import views


app_name = 'products'


urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('create/', views.ProductCreate.as_view(), name='product-create'),
    path('<slug:slug>/', views.ProductDetialView.as_view(), name='product-detail'),
    path('<slug:slug>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('<slug:slug>/delete/', views.ProductDeleteView.as_view(), name='product-delete')
]