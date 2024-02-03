from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.product, name='product'),
    path('add/', views.add, name='add'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('productDetail/<int:productID>/', views.productDetail, name='productDetail'),
    path('update/<int:productID>/', views.update, name='update'),
    path('about/', views.about, name='about'),
    path('category/', views.category, name='category'),
]
