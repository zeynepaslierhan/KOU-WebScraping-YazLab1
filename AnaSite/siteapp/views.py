from django.shortcuts import render
import pymongo
from bson.objectid import ObjectId

# Create your views here.

# Cluster-WebScraping için bağlantı sağlandı (Compass yardımı ile). (username: zeyneperhan password: 20012022)
myclient = pymongo.MongoClient("mongodb://zeynep:20012022@ac-akv12vk-shard-00-00.6erqfem.mongodb.net:27017,ac-akv12vk-shard-00-01.6erqfem.mongodb.net:27017,ac-akv12vk-shard-00-02.6erqfem.mongodb.net:27017/?ssl=true&replicaSet=atlas-8ffx15-shard-0&retryWrites=true&w=majority") 

# Kullanacağımız veritabanı için erişim sağladık.
mydb = myclient["Bilgisayar"]

# Bilgisayar Veritabanındaki Amazon koleksiyonuna erişim sağladık
mycollection= mydb["siteapp_liste"]

def index(request):                                         #urls'de tanımlanan pathlerin html dosyalarıyla bağlantısı sağlandı.
    
    return render(request, 'siteapp/index.html')

                                                            # daha sonra templates/siteapp klasörü altına geçilip ilgili .html dosyaları oluşturuldu    
                                                            
def pc_list(request):
    bilg_list = mycollection.find({})
    return render(request, 'siteapp/index.html',
                  {'bilg_list': bilg_list})
    
def product_page(request,index):
    product = mycollection.find({ "index" : index})
    return render(request, 'siteapp/product.html',
                  {'product':product})

def productsList_byBrand(request,brand):
    bilg_list = mycollection.aggregate([{"$match": {"Marka":brand}}])
    return render(request, 'siteapp/index.html',{'bilg_list':bilg_list})

def productsList_byWeb(request,web):
    bilg_list = mycollection.aggregate([{"$match": {"Marka":web}}])
    return render(request, 'siteapp/index.html',{'bilg_list':bilg_list})

