from ast import Delete
import pymongo 
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import validators

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}

driver_path = 'C:\\Users\\zerha\\Downloads\\chromedriver.exe'


# Cluster-WebScraping için bağlantı sağlandı. (username: zeyneperhan password: 20012022)
myclient = pymongo.MongoClient("mongodb://zeynep:20012022@ac-akv12vk-shard-00-00.6erqfem.mongodb.net:27017,ac-akv12vk-shard-00-01.6erqfem.mongodb.net:27017,ac-akv12vk-shard-00-02.6erqfem.mongodb.net:27017/?ssl=true&replicaSet=atlas-8ffx15-shard-0&retryWrites=true&w=majority") 

# Kullanacağımız veritabanı için erişim sağladık.
mydb = myclient["Bilgisayar"]

# Bilgisayar Veritabanındaki Amazon koleksiyonuna erişim sağladık
mycollection= mydb["Products"]

def trendyol(product):
    
    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Trendyol.Mevcut": False}})

    name = product['Name']

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    trednyol_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    trednyol_veri_girisi.send_keys(name+" "+" site:trendyol.com")
    time.sleep(4)
    trednyol_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(4)
    trendyol_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
    trendyol_tikla.click()
    time.sleep(4)
    product_url = browser.current_url
    print(product_url)
    

    product_soup = BeautifulSoup(browser.page_source, 'html.parser')

    product_name=product_soup.h1.text
    print(product_name)

    if product_soup.find("span",{"class":"prc-dsc"}) is not None:
        product_price = product_soup.find("span",{"class":"prc-dsc"}).text

    else:
        product_price= None

    print(product_price)

    if product_price is not None:
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Trendyol.Price": product_price}})
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Trendyol.URL": product_url}})
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Trendyol.Mevcut": True}})

def hepsiBurada(product):

    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"HepsiBurada.Mevcut": False}})
    name = product['Name']

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    hepsiBurada_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    hepsiBurada_veri_girisi.send_keys(name+" "+" site:hepsiburada.com")
    time.sleep(4)

    hepsiBurada_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(4)
    hepsiBurada_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
    hepsiBurada_tikla.click()
    time.sleep(4)
    product_url = browser.current_url
    print(product_url)
    

    product_soup = BeautifulSoup(browser.page_source, 'html.parser')

    product_name=product_soup.h1.text
    print(product_name)

    if product_soup.find("del",{"id":"originalPrice"}) is not None:
        product_price = product_soup.find("del",{"id":"originalPrice"}).text

    else:
        product_price= None

    print(product_price)

    if product_price is not None:
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"HepsiBurada.Price": product_price}})
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"HepsiBurada.URL": product_url}})
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"HepsiBurada.Mevcut": True}})

def cicekSepetiExtra(product):
    
    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"cicekSepetiExtra.Mevcut": False}})
    name = product['Name']

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    cicekSepetiExtra_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    cicekSepetiExtra_veri_girisi.send_keys(name+" "+" site:ciceksepeti.com")
    time.sleep(4)
    cicekSepetiExtra_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(4)
    cicekSepetiExtra_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
    cicekSepetiExtra_tikla.click()
    time.sleep(4)
    product_url = browser.current_url
    print(product_url)
    

    product_soup = BeautifulSoup(browser.page_source, 'html.parser')

    product_name=product_soup.h1.text
    print(product_name)

    if browser.find_element("css selector", "#productDetailSend > div > div > div:nth-child(2) > div.product__main-info-right.js-set-date-base-campaing-class > div.product__not-available.js-product-not-available.js-no-stock"):
        print("Stok bitmiş")
    else:
        product_price = browser.find_element("css selector","#productDetailSend > div > div > div:nth-child(2) > div.product__main-info-right.js-set-date-base-campaing-class > div:nth-child(2) > div > div.product__info-wrapper--right > div.product__info__price.js-default-price > div.product__info__new-price.js-price-container > div.product__info__new-price__integer.js-price-integer")
        product_priceText = product_price.get_attribute("innerHTML")


        print(product_priceText)
        
        
        if product_price is not None:
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"cicekSepetiExtra.Price": product_priceText}})
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"cicekSepetiExtra.URL": product_url}})
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"cicekSepetiExtra.Mevcut": True}})

def vatanBilgisayar(product):
    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"vatanBilgisayar.Mevcut": False}})
    name = product['Name']

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    vatanBilgisayar_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    vatanBilgisayar_veri_girisi.send_keys(name+" "+" site:vatanbilgisayar.com")
    time.sleep(4)
    vatanBilgisayar_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(4)
    vatanBilgisayar_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
    vatanBilgisayar_tikla.click()
    time.sleep(4)
    product_url = browser.current_url
    print(product_url)
    

    product_soup = BeautifulSoup(browser.page_source, 'html.parser')

    product_name=product_soup.h1.text
    print(product_name)

    if product_soup.find("span",{"class":"product-list__price"}) is not None:
        product_price = product_soup.find("span",{"class":"product-list__price"}).text

    else:
        product_price= None

    print(product_price)

    if product_price is not None:
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"vatanBilgisayar.Price": product_price}})
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"vatanBilgisayar.URL": product_url}})
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"vatanBilgisayar.Mevcut": True}})

def amazon(product):
    
    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Amazon.Mevcut": False}})

    name = product['Name']

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    amazon_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    amazon_veri_girisi.send_keys(name+" "+" site:amazon.com.tr")
    time.sleep(4)
    amazon_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(4)
    amazon_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
    amazon_tikla.click()
    time.sleep(4)
    product_url = browser.current_url
    print(product_url)
    

    product_soup = BeautifulSoup(browser.page_source, 'html.parser')

    product_name=product_soup.h1.text
    print(product_name)

    product_price = browser.find_element("css selector","#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > span > span.a-offscreen")
    product_priceText = product_price.get_attribute("innerHTML")

    print(product_priceText)

    if product_price is not None:
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Amazon.Price": product_priceText}})
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Amazon.URL": product_url}})
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Amazon.Mevcut": True}})

def teknosa(product):
    
    name = product['Name']
    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"teknosa.Mevcut": False}})
    

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    teknosa_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    teknosa_veri_girisi.send_keys(name+" "+" site:teknosa.com")
    time.sleep(4)
    teknosa_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(4)
    teknosa_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
    teknosa_tikla.click()
    time.sleep(4)
    product_url = browser.current_url
    print(product_url)
    

    product_soup = BeautifulSoup(browser.page_source, 'html.parser')

    product_name=product_soup.h1.text
    print(product_name)

    product_price = browser.find_element("css selector","#pdp-main > div.pdp-block2.pdpGeneralWidth > div.pdp-details > div.addtocart-component > div > div.AddToCart-AddToCartAction > div > div.pdp-amount.prc-last-2 > div > div > span")
    product_priceText = product_price.get_attribute("innerHTML")

    print(product_priceText)

    if product_price is not None:
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"teknosa.Price": product_priceText}})
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"teknosa.URL": product_url}})
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"teknosa.Mevcut": True}})


mycollectionComputer = mydb['BilgisayarismiVeFotografı']

for product in mycollectionComputer.find({}):
    mycollection.delete_many({})
    mycollection.insert_one({"Name" : product['Name'],"Img" : product['Img']})
    hepsiBurada(product)
    teknosa(product)
    amazon(product)
    vatanBilgisayar(product)
    cicekSepetiExtra(product)
    trendyol(product)