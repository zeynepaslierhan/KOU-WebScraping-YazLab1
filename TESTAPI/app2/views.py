from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app2/list.html')        #urls'de tanımlanan pathlerin html dosyalarıyla bağlantısı sağlandı.

def detaylar(request):
    return render(request, 'app2/detaylar.html')        # daha sonra templates/app2 klasörü altına geçilip ilgili .html dosyaları oluşturuldu

def search(request):
    return render(request, 'app2/search.html')
