from django.urls import path
from . import views
from bson.objectid import ObjectId

# http://127.0.0.1:8000

urlpatterns = [
    path('', views.pc_list, name='list-pc'),
    path('byıd/<int:index>/', views.product_page, name='product_page'),
    path('byBrand/<str:brand>/', views.productsList_byBrand , name='productsList_byBrand'),
    path('byWeb/<str:web>/', views.productsList_byWeb , name='productsList_byWeb')
]