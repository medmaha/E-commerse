
from django.urls import path, include
from store import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='product_all'),
    path('detail=<slug:pruduct_slug>/', views.product_detail, name='product_detail'),
    path('category=<slug:category_slug>/', views.category_list, name='category_list')
] 