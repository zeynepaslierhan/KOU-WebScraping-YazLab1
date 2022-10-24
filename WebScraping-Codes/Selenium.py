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


    name = product['Name']

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    trednyol_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    trednyol_veri_girisi.send_keys(name+" "+" site:trendyol.com")

    trednyol_veri_girisi.send_keys(Keys.ENTER)

    trendyol_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
    trendyol_tikla.click()

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

def hepsiBurada(product):


    name = product['Name']

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    hepsiBurada_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    hepsiBurada_veri_girisi.send_keys(name+" "+" site:hepsiburada.com")

    hepsiBurada_veri_girisi.send_keys(Keys.ENTER)

    hepsiBurada_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
    hepsiBurada_tikla.click()

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

def cicekSepetiExtra(product):
    
    name = product['Name']

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    cicekSepetiExtra_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    cicekSepetiExtra_veri_girisi.send_keys(name+" "+" site:ciceksepeti.com")

    cicekSepetiExtra_veri_girisi.send_keys(Keys.ENTER)

    cicekSepetiExtra_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
    cicekSepetiExtra_tikla.click()

    product_url = browser.current_url
    print(product_url)
    

    product_soup = BeautifulSoup(browser.page_source, 'html.parser')

    product_name=product_soup.h1.text
    print(product_name)

    if product_soup.find("div",{"class":"product__info__new-price__integer js-price-integer"}) is not None:
        product_price = product_soup.find("div",{"class":"product__info__new-price__integer js-price-integer"}).text

    else:
        product_price= None

    print(product_price)
    
    
    if product_price is not None:
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"cicekSepetiExtra.Price": product_price}})
        mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"cicekSepetiExtra.URL": product_url}})

def vatanBilgisayar(product):
    name = product['Name']

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    vatanBilgisayar_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    vatanBilgisayar_veri_girisi.send_keys(name+" "+" site:vatanbilgisayar.com")

    vatanBilgisayar_veri_girisi.send_keys(Keys.ENTER)

    vatanBilgisayar_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
    vatanBilgisayar_tikla.click()

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


for product in mycollection.find({}):
    trendyol(product)
    hepsiBurada(product)
    cicekSepetiExtra(product)
    vatanBilgisayar(product)