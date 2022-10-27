import pymongo

# Cluster-WebScraping için bağlantı sağlandı. (username: zeyneperhan password: 20012022)
myclient = pymongo.MongoClient("mongodb://zeynep:20012022@ac-akv12vk-shard-00-00.6erqfem.mongodb.net:27017,ac-akv12vk-shard-00-01.6erqfem.mongodb.net:27017,ac-akv12vk-shard-00-02.6erqfem.mongodb.net:27017/?ssl=true&replicaSet=atlas-8ffx15-shard-0&retryWrites=true&w=majority") 

# Kullanacağımız veritabanı için erişim sağladık.
mydb = myclient["Bilgisayar"]

mycollection= mydb["Products"]
mycollectionSite= mydb["siteapp_Liste"]

def VeriAktar():
    
    mycollectionSite.delete_many({})
    item={}

    for product in mycollection.find({}):

       item['Name'] = product['Name']

    item['Img'] = product['Img']

    item['index'] = product['index']

    details = product['Details']    
    item['Marka'] = details['Marka']
    item['BellekHızı'] = details['BellekHızı']
    item['HDMI'] = details['HDMI']
    item['EkranKartıBellekTipi'] = details['EkranKartıBellekTipi']
    item['Renk'] = details['Renk']
    item['RamTipi'] = details['RamTipi']

    if "HepsiBurada" in product: 
      HepsiBurada = product['HepsiBurada']

      if HepsiBurada['Mevcut'] == True:

        item['HepsiBuradaPrice'] = HepsiBurada['Price']
        item['HepsiBuradaURL'] = HepsiBurada['URL']
        item['HepsiBuradaRating'] = None

      else:
        item['HepsiBuradaPrice'] = None
        item['HepsiBuradaURL'] = None
        item['HepsiBuradaRating'] = None
    else:
      item['HepsiBuradaPrice'] = None
      item['HepsiBuradaURL'] = None
      item['HepsiBuradaRating'] = None

    if "teknosa" in product: 
      teknosa = product['teknosa']

      if teknosa['Mevcut'] == True:

        item['teknosaPrice'] = teknosa['Price']
        item['teknosaURL'] = teknosa['URL']                
        item['teknosaRating'] = None

      else:
        item['teknosaPrice'] = None
        item['teknosaURL'] = None
        item['teknosaRating'] = None
    else:
      item['teknosaPrice'] = None
      item['teknosaURL'] = None
      item['teknosaRating'] = None

    if "Amazon" in product: 
      Amazon = product['Amazon']

      if Amazon['Mevcut'] == True:

        item['AmazonPrice'] = Amazon['Price']
        item['AmazonURL'] = Amazon['URL']
        item['AmazonRating'] = None   
      else:
          item['AmazonRating'] = None
          item['AmazonURL'] = None
          item['AmazonPrice'] = None
    else:
      item['AmazonRating'] = None
      item['AmazonURL'] = None
      item['AmazonPrice'] = None

    if "vatanBilgisayar" in product: 
      vatanBilgisayar = product['vatanBilgisayar']

      if vatanBilgisayar['Mevcut'] == True:

        item['vatanBilgisayarPrice'] = vatanBilgisayar['Price']
        item['vatanBilgisayarURL'] = vatanBilgisayar['URL']
        item['vatanBilgisayarRating'] = None

      else:
        item['vatanBilgisayarPrice'] = None
        item['vatanBilgisayarURL'] = None
        item['vatanBilgisayarRating'] = None
    else:
      item['vatanBilgisayarPrice'] = None
      item['vatanBilgisayarURL'] = None
      item['vatanBilgisayarRating'] = None

    if "cicekSepetiExtra" in product:  
      cicekSepetiExtra = product['cicekSepetiExtra']

      if cicekSepetiExtra['Mevcut'] == True:
        item['cicekSepetiExtraPrice'] = cicekSepetiExtra['Price']
        item['cicekSepetiExtraURL'] = cicekSepetiExtra['URL']
        item['cicekSepetiExtraRating'] = None
      else:
        item['cicekSepetiExtraPrice'] = None
        item['cicekSepetiExtraURL'] = None
        item['cicekSepetiExtraRating'] = None
    else:
      item['cicekSepetiExtraPrice'] = None
      item['cicekSepetiExtraURL'] = None
      item['cicekSepetiExtraRating'] = None

    if "Trendyol" in product:
      Trendyol = product['Trendyol']

      if Trendyol['Mevcut'] == True:

        item['TrendyolPrice'] = Trendyol['Price']
        item['TrendyolURL'] = Trendyol['URL']
        item['TrendyolRating'] = None
      else:
        item['TrendyolPrice'] = None
        item['TrendyolURL'] = None
        item['TrendyolRating'] = None
    else:
      item['TrendyolPrice'] = None
      item['TrendyolURL'] = None
      item['TrendyolRating'] = None

    if "n11" in product:
      n11 = product['n11']

      if n11['Mevcut'] == True:

        item['n11Price'] = n11['Price']
        item['n11URL'] = n11['URL']
        item['n11Rating'] = None
      else:
        item['n11Price'] = None
        item['n11URL'] = None
        item['n11Rating'] = None
    else:
      item['n11Price'] = None
      item['n11URL'] = None
      item['n11Rating'] = None       
        
 
    mycollectionSite.insert_one(item)
    item.clear()
