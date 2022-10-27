from django.contrib import admin
from .models import *
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer
from django.http import HttpResponse, JsonResponse
from django.contrib import admin
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt

import WebScraping
import VeriAktarımı


@admin.register(Ürün)

class MyModelModelAdmin(ExtraButtonsMixin, admin.ModelAdmin):

    @button(permission='demo.add_demomodel1',
            change_form=True,
            html_attrs={'style': 'background-color:#88FF88;color:black'})
    
    def WebScraping(self, request):
        self.message_user(request, 'Web Scraping başlatılıyor')
        WebScraping.VerileriKompleDeğiştirme()
        # Optional: returns HttpResponse
        return HttpResponseRedirectToReferrer(request)
    
    @button(permission='demo.add_demomodel1',
            change_form=True,
            html_attrs={'style': 'background-color:#88FF88;color:black'})
    
    def Güncelleme(self, request):
        self.message_user(request, 'Fiyat Güncellemesi başlatılıyor')
        WebScraping.KayıtlıVerilerinFiyatlarınıGüncelleme()
        # Optional: returns HttpResponse
        return HttpResponseRedirectToReferrer(request)
    
list_display = ("name", "marka")        
