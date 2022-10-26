from ast import Delete
import pymongo 
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import validators

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
    trednyol_veri_girisi.send_keys(Keys.ENTER)

    try:
        trendyol_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
        trendyol_tikla.click()
        product_url = browser.current_url
        

        product_soup = BeautifulSoup(browser.page_source, 'html.parser')
        if product_soup.find("span",{"class":"prc-dsc"}) is not None:
            product_price = product_soup.find("span",{"class":"prc-dsc"}).text

        else:
            product_price= None

        if product_price is not None:
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Trendyol.Price": product_price}})
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Trendyol.URL": product_url}})
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Trendyol.Mevcut": True}})

        try:
            product_rating = browser.find_element("css selector","#product-detail-app > div > div.flex-container > div.product-container > div:nth-child(2) > div.container-right-content > div.pr-in-w > div > div > div.pr-in-ratings > div > div.review-tooltip > div.review-tooltip-content > div > span > span")
            product_ratingText = product_rating.get_attribute("innerHTML")
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Trendyol.Rating": product_ratingText}})
                
        except NoSuchElementException:
            print("Exception Handled")
    except NoSuchElementException:
        print("Exception Handled")

def hepsiBurada(product):

    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"HepsiBurada.Mevcut": False}})
    name = product['Name']

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")
    hepsiBurada_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    hepsiBurada_veri_girisi.send_keys(name+" "+" site:hepsiburada.com")
    hepsiBurada_veri_girisi.send_keys(Keys.ENTER)

    try:
        hepsiBurada_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
        hepsiBurada_tikla.click()
        product_url = browser.current_url
        

        product_soup = BeautifulSoup(browser.page_source, 'html.parser')

        if product_soup.find("del",{"id":"originalPrice"}) is not None:
            product_price = product_soup.find("del",{"id":"originalPrice"}).text

        else:
            product_price= None

        if product_price is not None:
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"HepsiBurada.Price": product_price}})
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"HepsiBurada.URL": product_url}})
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"HepsiBurada.Mevcut": True}})
        
        try:
            product_rating = browser.find_element("css selector","#productReviews > span.rating-star")
            product_ratingText = product_rating.get_attribute("innerHTML")
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"HepsiBurada.Rating": product_ratingText}})
                
        except NoSuchElementException:
            print("Exception Handled")
    except NoSuchElementException:
        print("Exception Handled")

def cicekSepetiExtra(product):
    
    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"cicekSepetiExtra.Mevcut": False}})
    name = product['Name']

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    cicekSepetiExtra_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    cicekSepetiExtra_veri_girisi.send_keys(name+" "+" site:ciceksepeti.com")
    cicekSepetiExtra_veri_girisi.send_keys(Keys.ENTER)

    try:
        cicekSepetiExtra_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
        cicekSepetiExtra_tikla.click()
        product_url = browser.current_url

        if browser.find_element("css selector", "#productDetailSend > div > div > div:nth-child(2) > div.product__main-info-right.js-set-date-base-campaing-class > div.product__not-available.js-product-not-available.js-no-stock"):
            print("Stok bitmiş")
        else:
            product_price = browser.find_element("css selector","#productDetailSend > div > div > div:nth-child(2) > div.product__main-info-right.js-set-date-base-campaing-class > div:nth-child(2) > div > div.product__info-wrapper--right > div.product__info__price.js-default-price > div.product__info__new-price.js-price-container > div.product__info__new-price__integer.js-price-integer")
            product_priceText = product_price.get_attribute("innerHTML")
            
            
            if product_price is not None:
                mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"cicekSepetiExtra.Price": product_priceText}})
                mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"cicekSepetiExtra.URL": product_url}})
                mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"cicekSepetiExtra.Mevcut": True}})
           
            try:
                product_rating = browser.find_element("css selector","#productDetailSend > div > div > div:nth-child(2) > div.product__main-info-right.js-set-date-base-campaing-class.has-date-base-discount > div:nth-child(2) > div > div.product__info-wrapper--right > div.product__header-summary.js-product-header-summary > div > div > p")
                product_ratingText = product_rating.get_attribute("innerHTML")
                mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"cicekSepetiExtra.Rating": product_ratingText}})
                
            except NoSuchElementException:
                print("Exception Handled")
    except NoSuchElementException:
        print("Exception Handled")

def vatanBilgisayar(product):
    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"vatanBilgisayar.Mevcut": False}})
    name = product['Name']

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    vatanBilgisayar_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    vatanBilgisayar_veri_girisi.send_keys(name+" "+" site:vatanbilgisayar.com")
    
    vatanBilgisayar_veri_girisi.send_keys(Keys.ENTER)
    

    try:
        vatanBilgisayar_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
        vatanBilgisayar_tikla.click()
        
        product_url = browser.current_url

        product_soup = BeautifulSoup(browser.page_source, 'html.parser')

        if product_soup.find("span",{"class":"product-list__price"}) is not None:
            product_price = product_soup.find("span",{"class":"product-list__price"}).text

        else:
            product_price= None

        if product_price is not None:
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"vatanBilgisayar.Price": product_price}})
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"vatanBilgisayar.URL": product_url}})
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"vatanBilgisayar.Mevcut": True}})

        
    except NoSuchElementException:
        print("Exception Handled")
    
def amazon(product):
    
    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Amazon.Mevcut": False}})

    name = product['Name']

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    amazon_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    amazon_veri_girisi.send_keys(name+" "+" site:amazon.com.tr")
    
    amazon_veri_girisi.send_keys(Keys.ENTER)
    

    try:
        amazon_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
        amazon_tikla.click()
        
        product_url = browser.current_url
        product_price = browser.find_element("css selector","#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > span > span.a-offscreen")
        product_priceText = product_price.get_attribute("innerHTML")

        if product_price is not None:
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Amazon.Price": product_priceText}})
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Amazon.URL": product_url}})
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Amazon.Mevcut": True}})

        try:
            product_rating = browser.find_element("css selector","#reviewsMedley > div > div.a-fixed-left-grid-col.a-col-left > div.a-section.a-spacing-none.a-spacing-top-mini.cr-widget-ACR > div.a-fixed-left-grid.AverageCustomerReviews.a-spacing-small > div > div.a-fixed-left-grid-col.aok-align-center.a-col-right > div > span > span")
            product_ratingText = product_rating.get_attribute("innerHTML")

            print(product_ratingText)
            mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Amazon.Rating": product_ratingText}})
                
        except NoSuchElementException:
            print("Exception Handled")

    except NoSuchElementException:
        print("Exception Handled")

def teknosa(product):
    
    name = product['Name']
    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"teknosa.Mevcut": False}})
    

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    try: 

        teknosa_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
        teknosa_veri_girisi.send_keys(name+" "+" site:teknosa.com")
        teknosa_veri_girisi.send_keys(Keys.ENTER)
        
        teknosa_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")

        if teknosa_tikla is not None:
            teknosa_tikla.click()
            
            product_url = browser.current_url

            product_price = browser.find_element("css selector","#pdp-main > div.pdp-block2.pdpGeneralWidth > div.pdp-details > div.addtocart-component > div > div.AddToCart-AddToCartAction > div > div.pdp-amount.prc-last-2 > div > div > span")
            product_priceText = product_price.get_attribute("innerHTML")

            if product_price is not None:
                mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"teknosa.Price": product_priceText}})
                mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"teknosa.URL": product_url}})
                mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"teknosa.Mevcut": True}})

            try:
                product_rating = browser.find_element("css selector","#ratings-summary > div.bv_avgRating_component_container.notranslate")
                product_ratingText = product_rating.get_attribute("innerHTML")

                print(product_ratingText)
                mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"teknosa.Rating": product_ratingText}})
                
            except NoSuchElementException:
                print("Exception Handled")
    except NoSuchElementException:
        print("Exception Handled")

def n11(product):
    
    name = product['Name']
    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"n11.Mevcut": False}})
    

    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")

    try: 

        n11_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
        n11_veri_girisi.send_keys(name+" "+" site:n11.com")
        n11_veri_girisi.send_keys(Keys.ENTER)
        
        n11_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")

        if n11_tikla is not None:
            n11_tikla.click()
            
            product_url = browser.current_url

            product_price = browser.find_element("css selector","#unf-p-id > div > div:nth-child(2) > div.unf-p-cvr > div.unf-p-left > div > div.unf-p-detail > div.unf-price-cover > div.price-cover > div.price > div > div > div > ins")
            product_priceText = product_price.get_attribute("innerHTML")

            if product_price is not None:
                mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"n11.Price": product_priceText}})
                mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"n11.URL": product_url}})
                mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"n11.Mevcut": True}})

            try:
                product_rating = browser.find_element("css selector","#unf-p-id > div > div:nth-child(2) > div.unf-p-cvr > div.unf-p-left > div > div.unf-p-detail > div.unf-p-title > div.proRatingHolder > div.ratingCont > strong")
                product_ratingText = product_rating.get_attribute("innerHTML")
                mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"n11.Rating": product_ratingText}})

            except NoSuchElementException:
                print("Exception Handled")
            
    except NoSuchElementException:
        print("Exception Handled")

def hepsiBuradaTam():
    mycollection.delete_many({})
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}

    # Verileri çekeceğimiz sitenin ana url'si
    base_url = 'https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98?sayfa={0}'

    #veriyi tutan dict
    item = {}
    j=0
    for i in range(1,2):
            
        print('Processing {0}...'.format(base_url.format(i)))
        print("-------------")    

        valid=validators.url(base_url.format(i))
                
        if valid==True:
            print("Valid url")
        else:
            print("Invalid url")
            print(base_url.format(i))
            continue
        
        response = requests.get(base_url.format(i), headers=headers)
        print(response)
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all('li',{'class': 'productListContent-zAP0Y5msy8OHn5z7T_K_'})

        for result in results:
            product_name = result.h3.text
            
            try:
                product_url = 'https://www.hepsiburada.com'+result.a.get("href")
                valid=validators.url(product_url)
                if valid==True:
                    browser = webdriver.Chrome(driver_path)
                    browser.get(product_url)
                    try:
                        img_url = browser.find_element("css selector","#productDetailsCarousel > div.owl-stage-outer > div > div.owl-item.active > a > picture > img").get_attribute("src")
                        item["Img"]= img_url
                    except NoSuchElementException:
                        print("Exception Handled")
                        continue
                    
                else:
                    print("Invalid url")
                    print(product_url)
                    continue    

                product_response = requests.get(product_url, headers=headers)
                            
                product_soup = BeautifulSoup(product_response.content, 'html.parser')

                product_details = product_soup.find_all("table",{"class":"data-list tech-spec"})

                for details in product_details:

                    informations = details.find_all("tr")

                    for info in informations:

                        try:               
                            label = info.find("th").text
                            value = info.find("span").text

                            item[label]=value            
                        except AttributeError:
                         continue
            except AttributeError:
                continue

            item["Name"] = product_name
            mycollection.insert_one(item)
            item.clear()

hepsiBuradaTam()
for product in mycollection.find({}):
    hepsiBurada(product)
    teknosa(product)
    amazon(product)
    vatanBilgisayar(product)
    cicekSepetiExtra(product)
    trendyol(product)
    n11(product)