from django.shortcuts import render
from .models import Bilg

# Create your views here.

def index(request):                                         #urls'de tanımlanan pathlerin html dosyalarıyla bağlantısı sağlandı.
    
    return render(request, 'siteapp/index.html')

                                                            # daha sonra templates/siteapp klasörü altına geçilip ilgili .html dosyaları oluşturuldu    
                                                            
def pc_list(request):
    bilg_list = Bilg.objects.all()
    
    return render(request, 'siteapp/index.html',
                  {'bilg_list': bilg_list})