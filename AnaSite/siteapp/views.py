from django.shortcuts import render
import pymongo
from bson.objectid import ObjectId

# Create your views here.

# Cluster-WebScraping için bağlantı sağlandı (Compass yardımı ile). (username: zeyneperhan password: 20012022)
myclient = pymongo.MongoClient("mongodb://zeynep:20012022@ac-akv12vk-shard-00-00.6erqfem.mongodb.net:27017,ac-akv12vk-shard-00-01.6erqfem.mongodb.net:27017,ac-akv12vk-shard-00-02.6erqfem.mongodb.net:27017/?ssl=true&replicaSet=atlas-8ffx15-shard-0&retryWrites=true&w=majority") 

# Kullanacağımız veritabanı için erişim sağladık.
mydb = myclient["Bilgisayar"]

# Bilgisayar Veritabanındaki Amazon koleksiyonuna erişim sağladık
mycollection= mydb["siteapp_Liste"]

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
    item={}
    products = mycollection.find({})
    if web == "Amazon":
        for product in products:
            if product['AmazonPrice'] is not None:
               item.append(product)
    if web == "Trendyol":
        for product in products:
            if product['TrendyolPrice'] is not None:
               item.append(product)
    if web == "VatanBilgisayar":
        for product in products:
            if product['vatanBilgisayarPrice'] is not None:
               item.append(product)
    if web == "Teknosa":
        for product in products:
            if product['teknosaPrice'] is not None:
               item.append(product)
    if web == "n11":
        for product in products:
            if product['n11Price'] is not None:
               item.append(product)
    if web == "ÇiçekSepeti":
        for product in products:
            if product['cicekSepetiExtraPrice'] is not None:
               item.append(product)
    if web == "Hepsiburada":
        for product in products:
            if product['HepsiBuradaPrice'] is not None:
               item.append(product)
    return render(request, 'siteapp/index.html',{'item' : item})

