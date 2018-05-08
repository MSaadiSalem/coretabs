from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('products/by_category/', views.products_by_category,
         name='products_by_category'),
    path('<str:slug>/', views.products_list, name='products_list'),
    path('products/<str:slug>/<int:id>/',
         views.product_detail, name='product_detail'),
]
