from django.shortcuts import render
import pymongo

# Create your views here.

# Cluster-WebScraping için bağlantı sağlandı (Compass yardımı ile). (username: zeyneperhan password: 20012022)
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 

# Kullanacağımız veritabanı için erişim sağladık.
mydb = myclient["testdatabase"]

# Bilgisayar Veritabanındaki Amazon koleksiyonuna erişim sağladık
mycollection= mydb["siteapp_bilg"]

def index(request):                                         #urls'de tanımlanan pathlerin html dosyalarıyla bağlantısı sağlandı.
    
    return render(request, 'siteapp/index.html')

                                                            # daha sonra templates/siteapp klasörü altına geçilip ilgili .html dosyaları oluşturuldu    
                                                            
def pc_list(request):
    bilg_list = mycollection.find({})
    print(bilg_list)
    return render(request, 'siteapp/index.html',
                  {'bilg_list': bilg_list})
    
def product_page(request,pcno):
    product = mycollection.find({"pcno": pcno})
    return render(request, 'siteapp/product.html',
                  {'product':product})
