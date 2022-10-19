"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path

# from django.conf.urls import include    # DepartmentsApp CRUD 

# http://127.0.0.1:8000/

urlpatterns = [                 # Girilen website urllerine pathler tanımlandı ve views.pye'ye geçildi.
    
    # boş bir path girildiği zaman index'e gitsin.
    path('', include('pages.urls')),    # pages app'inin urlsini ekler. Başka bir url için '' içerisine o url'nin admin/ gibi ismi yazılmalıdır.
    path('app2/', include('app2.urls')), # app2 url eklemesi
    path('admin/', admin.site.urls),
    
    # re_path(r'^',include('pages.urls'))
]
