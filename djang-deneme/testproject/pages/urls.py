from django.urls import path, re_path
from . import views         # CRUD için
from pages import views        # CRUD için

# http://127.0.0.1:8000

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    
    
    #re_path(r'^departments$', views.departmentsApi),            # departments crud
    #re_path(r'^departments/([0-9]+)', views.departmentsApi),                     # departments crud
    
    #re_path(r'^employee$', views.employeeApi),            # employees crud
    #re_path(r'^employee/([0-9]+)', views.employeeApi)                        # employees crud
    
]