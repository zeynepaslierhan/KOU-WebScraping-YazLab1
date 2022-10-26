from django.urls import path
from . import views
from bson.objectid import ObjectId

# http://127.0.0.1:8000

urlpatterns = [
    path('', views.pc_list, name='list-pc'),
    path('<str:name>/', views.product_page, name='product_page')

]