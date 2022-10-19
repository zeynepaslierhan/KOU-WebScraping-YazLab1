from re import search
from django.urls import path
from . import views

# 127.0.0.1:8000/app2
# 127.0.0.1:8000/app2/2
# 127.0.0.1:8000/app2/search

urlpatterns = [
    path('', views.index, name = 'app2'),                           # Girilen website urllerine pathler tanımlandı ve views.pye'ye geçildi.
    path('<int:app2_id>', views.detaylar, name= 'detaylar'),
    path('search', views.search, name= 'search')
]


