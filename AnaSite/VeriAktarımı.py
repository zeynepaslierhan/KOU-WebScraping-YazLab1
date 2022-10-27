import pymongo

# Cluster-WebScraping için bağlantı sağlandı. (username: zeyneperhan password: 20012022)
myclient = pymongo.MongoClient("mongodb://zeynep:20012022@ac-akv12vk-shard-00-00.6erqfem.mongodb.net:27017,ac-akv12vk-shard-00-01.6erqfem.mongodb.net:27017,ac-akv12vk-shard-00-02.6erqfem.mongodb.net:27017/?ssl=true&replicaSet=atlas-8ffx15-shard-0&retryWrites=true&w=majority") 

# Kullanacağımız veritabanı için erişim sağladık.
mydb = myclient["Bilgisayar"]

mycollection= mydb["Products"]
mycollectionSite= mydb["siteapp_ürünler"]

def VeriAktar():
    
    mycollectionSite.delete_many({})
    item={}
    for product in mycollection:

        item['Name'] = product['Name']
        
        item['Img'] = product['Img']

        item[''] = product['']

        item[''] = product['']

        item[''] = product['']

        item[''] = product['']

        item[''] = product['']

        item[''] = product['']

        item[''] = product['']