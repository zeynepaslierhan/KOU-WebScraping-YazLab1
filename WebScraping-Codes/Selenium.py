from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}

driver_path = 'C:\\Users\\zerha\\Downloads\\chromedriver.exe'
browser = webdriver.Chrome(driver_path)

bilgisayar = "NX.HE3EY.00C"

def trendyol():
    browser.get("https://www.google.com/")

    trednyol_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    trednyol_veri_girisi.send_keys(bilgisayar+" "+" site:trendyol.com")

    trednyol_veri_girisi.send_keys(Keys.ENTER)

    trendyol_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
    trendyol_tikla.click()

    product_url = browser.page_source
            
    product_soup = BeautifulSoup(product_url, 'html.parser')

    product_name=product_soup.h1.text
    print(product_name)

    if product_soup.find("span",{"class":"prc-dsc"}) is not None:
        product_price = product_soup.find("span",{"class":"prc-dsc"}).text

    else:
        product_price= None

    print(product_price)

def n11():

    browser.get("https://www.google.com/")

    n11_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    n11_veri_girisi.send_keys(bilgisayar+" "+" site:n11.com")

    n11_veri_girisi.send_keys(Keys.ENTER)

    n11_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
    n11_tikla.click()

    product_url = browser.page_source
            
    product_soup = BeautifulSoup(product_url, 'html.parser')
    
    if product_soup.find("div",{"class":"newPrice"}) is not None:
        product_price = product_soup.find("div",{"class":"newPrice"}).text
    else:
        product_price= None

    print(product_price)

    if product_soup.find("div",{"class":"ratingCont "}) is not None:
        rating =product_soup.find("div",{"class":"ratingCont "}).find("strong").text
    if rating == "0":
        rating = "Derecelendirilmemiş"
    else:
        rating = "Derecelendirilmemiş"

    print(rating)

print("---------------------")
trendyol()
print("---------------------")
n11()
print("---------------------")