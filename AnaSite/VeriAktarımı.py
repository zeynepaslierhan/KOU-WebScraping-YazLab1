import pymongo

# Cluster-WebScraping için bağlantı sağlandı. (username: zeyneperhan password: 20012022)
myclient = pymongo.MongoClient("mongodb://zeynep:20012022@ac-akv12vk-shard-00-00.6erqfem.mongodb.net:27017,ac-akv12vk-shard-00-01.6erqfem.mongodb.net:27017,ac-akv12vk-shard-00-02.6erqfem.mongodb.net:27017/?ssl=true&replicaSet=atlas-8ffx15-shard-0&retryWrites=true&w=majority") 

# Kullanacağımız veritabanı için erişim sağladık.
mydb = myclient["Bilgisayar"]

mycollection= mydb["Products"]
mycollectionSite= mydb["siteapp_ürün"]

def VeriAktar():
    
    mycollectionSite.delete_many({})
    item={}

    for product in mycollection.find({}):

        item['id']= product['index']

        item['Name'] = product['Name']
        
        item['Img'] = product['Img']

        item['index'] = product['index']

        
        item['Marka'] = None
        item['BellekHızı'] = None
        item['HDMI'] = None
        item['EkranKartıBellekTipi'] = None
        item['Renk'] = None
        item['RamTipi'] = None

        if "HepsiBurada" in product:
          HepsiBurada = product['HepsiBurada']

          if HepsiBurada['Mevcut'] == True:

              item['HepsiBuradaPrice'] = HepsiBurada['Price']

              item['HepsiBuradaURL'] = HepsiBurada['URL']

              if "Rating" in HepsiBurada:
                item['HepsiBuradaRating'] = HepsiBurada['Rating']
              else:
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

                if "Rating" in teknosa:
                  item['teknosaRating'] = teknosa['Rating']
                else:
                  item['teknosaRating'] = None

            else:
                item['teknosaPrice'] = None

                item['teknosaURL'] = None

                item['teknosaRating'] = None 


          if "Amazon" in product:
            Amazon = product['HepsiBurada']

            if Amazon['Mevcut'] == True:

                item['AmazonPrice'] = Amazon['Price']

                item['AmazonURL'] = Amazon['URL']
                
                if "Rating" in Amazon:
                  item['AmazonRating'] = Amazon['Rating']
                else:
                  item['AmazonRating'] = None

                
            else:
                item['AmazonRating'] = None

                item['AmazonURL'] = None

                item['AmazonPrice'] = None


          if "vatanBilgisayar" in product:
            vatanBilgisayar = product['vatanBilgisayar']

            if vatanBilgisayar['Mevcut'] == True:

                item['vatanBilgisayarPrice'] = vatanBilgisayar['Price']

                item['vatanBilgisayarURL'] = vatanBilgisayar['URL']

                if "Rating" in vatanBilgisayar:
                  item['vatanBilgisayarRating'] = vatanBilgisayar['Rating']
                else:
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

                if "Rating" in cicekSepetiExtra:
                  item['cicekSepetiExtraRating'] = cicekSepetiExtra['Rating']
                else:
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

                if "Rating" in Trendyol:
                  item['TrendyolRating'] = Trendyol['Rating']
                else:
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

                if "Rating" in n11:
                  item['n11Rating'] = n11['Rating']
                else:
                  item['n11Rating'] = None
            else:
                item['n11Price'] = None

                item['n11URL'] = None

                item['n11Rating'] = None        
        
        
 
        mycollectionSite.insert_one(item)
        item.clear()