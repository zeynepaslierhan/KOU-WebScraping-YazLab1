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
    trendyol = product['Trendyol']

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    trednyol_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    trednyol_veri_girisi.send_keys(name+" "+" site:trendyol.com")

    trednyol_veri_girisi.send_keys(Keys.ENTER)

    trendyol_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
    trendyol_tikla.click()

    product_url = browser.current_url
    print(product_url)
    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Trendyol.URL": product_url}})

    product_soup = BeautifulSoup(browser.page_source, 'html.parser')

    product_name=product_soup.h1.text
    print(product_name)

    if product_soup.find("span",{"class":"prc-dsc"}) is not None:
        product_price = product_soup.find("span",{"class":"prc-dsc"}).text

    else:
        product_price= None

    print(product_price)
    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Trendyol.Price": product_price}})
    

for product in mycollection.find({}):
    trendyol(product)