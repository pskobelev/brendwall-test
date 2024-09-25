from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='product_form'),
    path('api/products/', views.get_products_list, name='products'),
    path('api/products/new/', views.add_new_product, name='create_product'),
]
