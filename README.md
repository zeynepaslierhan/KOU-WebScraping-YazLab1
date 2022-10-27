# .Net Core ile Web Scraping E-Ticaret

## İçerik

1. Proje Tanıtımı
2. Kullanılan Araçların Açıklamaları
3. Proje Algoritması

## Giriş

Trendyol, Hepsiburada, n11, Amazon, gibi e ticaret sitelerinden istenilen ürüne ait bilgilerin yer aldığı bir veritabanı oluşturulacak ve bu veritabanından istenilen bilgileri web sayfası üzerinde gösterilecektir.

E-Ticaret sitelerine benzer yapıya sahiptir ama sadece bilgisayar kategorisinden oluşturulmuştur.

E-ticaret sitesinin kontrolü Admin tarafından sağlanmaktadır. Bu adminin yetkileri sayesinde:

- Sadece Admin tarafından yapılan işlemler:
    - Bir notebook ürünlerinin fiyatının değiştirilmesi
    - Notebook ürününe ait bir kaydın kaldırılması
    - Yeni notebook ürünlerinin eklenmesi
    - Notebook ürünlerinin puanında değişiklik yapılması
- Web Scraping ile veri yönetme:
    - Ürün bilgilerinin güncellenmesi

## Arayüz

Ana Sayfada veritabanında yer alan tüm kayıtlar lislenmiştir. Listelenirken her ürünün ismi sahip olduğu tüm özellikleri kapsıyor ve ismine tıklandığında ilgili ürünün detaylı bilgisine ulaşılıyor. İsminin altında ürüne ait en düşük 3 fiyat sıralanmakta ve bu 3 fiyatın olduğu e-ticaret sitesinin linki bulunmaktadır.

Layout kısmında herhangi bir ürünle ilgili arama kısmı bulunuyor. Buradan ürünün ismi, modeli ya da bulunduğu e-ticaret sitesine göre arama yapılabiliyor. Arama yanlışı olduğunda sistem düzeltilmiş öneride bulunuyor.

Ana Sayfanın sol tarafında ise dinamik filtreleme kısmı bulunmakta. En düşük fiyattan en yüksek fiyata, en yüksek fiyattan en düşük fiyata ve en 
yüksek puandan en düşük fiyata şeklinde sıralama işlemleri ise arama kısmının altında mevcuttur. Laptop bilgilerinin yer aldığı alanda fiyat bilgisi için de aynı durum geçerlidir.

Arayüz’ü tasarlarken W3school css templates kullandık. İstediğimiz sadeleştirilmeleri yaptıktan sonra ilave olarak ihtiyacımız olan özellikleri başka ücretsiz şablonlardan sağladık.

Sayfalar: 

1. Ana Sayfa: Tüm verilerin listelendiği, filtrelenerek sıralandığı sayfa.
2. Login: Sistemde kayıtlı adminin giriş yaptığı sayfa.
3. Admin Paneli: Adminin verileri kontrol ettiği sayfa.

## Django yapısı

### Django projesinin oluşturulması

1. Gerekli paketlerin yüklenmesi
    
    ```bash
    pip install django
    pip install djongo
    pip install pymongo
    ```
    
2. Projenin oluşturulması
    1. Proje Database’e 2. görseldeki DATABASES değişkeni içerisindeki yapı aracılığıyla erişim sağlar.
    
    ```python
    django-admin startproject projeismi
    python manage.py startapp appismi // oluşturulan app aşağıdaki gibi, settings.py içerisindeki installed_apps klasörüne yazılmalıdır.
    ```
    
    ![Untitled](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/Untitled.png)
    
    ![database connection.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/database_connection.png)
    
3. Web sayfasının URL’leri tanımlanır.
    
    ![url_proje.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/url_proje.png)
    
4. Html bağlantı işlemleri ve sayfaya yansıtılması
    1. Tanımlanan url’ye html dosyalarının bağlanması için oluşturduğumuz app içindeki “views.py” dosyasına erişilir ve request işlemleri oluşturulur.
    2. HTML sayfalarının database ile bağlantı kurması için gerekli bağlantılar görseldeki gibi yapılır (MongoDB)
        
        ![views.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/views.png)
        
5.  Database’de kullanacağımız Table yapısı, app içerisindeki [models.py](http://models.py) içerisinde oluşturulur
    
    ![model.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/model.png)
    
    ```python
    def __str__(self):
            return f"{self.name}, {self.marka}"
    ```
    
    def yapısı admin panelindeki görüntülemede okuma kolaylığı sağlamak için kişiselleştirilebilir. (görseldeki örnek ürünün isim ve marka değerlerini 2 column şeklinde admin panelinde görüntüler. Admin Panel Kısım: X)
    
6. Oluşturulan Table yapısının ve diğer değişikliklerin database’e yansıtılması:
    1. migration oluşturma
        
        ![makemigrations.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/makemigrations.png)
        
        > “Not Implemented Error: Database objects do not implement truth value testing or bool().” hatası almamak için: `pip install pymongo==3.12.3`
        > 
    2. migration’ı gönderme
        
        ![migrate.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/migrate.png)
        
    3. Bunları denetlemek ve admin sayfasına erişmek için admin kullanıcısı oluşturma (migration oluşturmadan bu aşamaya geçmeyiniz!!!)
        
        ![admincreatesuperuser.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/admincreatesuperuser.png)
        
7. Projeye ekleyeceğimiz HTML dosyaları okunurluk ve genel işleyiş kolaylığı açısından proje içerisine açılan “templates” klasörü içerisindeki “appismi” klasörüne yerleştirilir. Templates klasörünün projeye tanıtılması ise aşağıdaki görseldeki gibidir.
    
    ![templates.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/templates.png)
    
8. HTML sayfalarına database üzerinden bilgi aktarabilmek için app içerisinde bulunan “urls.py” içerisine gerekli bağlantılar yapılır.
    
    ![url_app.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/url_app.png)
    
9. Admin sayfasına bağlantı sağlamak ve düzenlemek için app içerisindeki “admin.py” içerisinde aşağıdaki işlemler uygulanır. (Gerektiği gibi kişiselleştirilebilir.)
    
    ![adminpy.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/adminpy.png)
    
10. Projenin örnek görüntüleri:
    
    ![homepage.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/homepage.png)
    
    ![productpage.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/productpage.png)
    
    ![adminpage.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/adminpage.png)
    
    ![adminindex.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/adminindex.png)
    
    ![adminlisting.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/adminlisting.png)
    
11. Admin sayfasının özelleştirilebilmesi (Web scraping için buton eklenmesi vb.) için hazır bir app kullandık.
    
    ![adminbutton.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/adminbutton.png)
    

## Web Scraping

**Web Scraping yaparken dikkat edilmesi gerekenler:,**

1. Üzerinde çalışılan sitenin URL geçerlilik kontrolü
    
    ```python
    import validators
    
    valid=validators.url('https://github.com/')
    
    if valid==True:
        print("Url geçerli")
    else:
        print("Url geçersiz")
    ```
    
2. Request atılan geçerli urlnin response değerinin 200 olup olmaması
    
    ```python
    response = requests.get(base_url.format(i), headers=headers)
    print(response)
    ```
    
3. Sitede istenilen verinin olup olmaması
    1. BeautifulSoap
        1. if ile None olup olmama
        2. try except yapısı
    2. Selenium
        1. try catch ile hata mesajlarını döndür. Bunun için ilgili kütüphaneleri ekle.
        
        ```python
        from selenium.common.exceptions import NoSuchElementException
        try:
        	veri = browser.find_element("css selector","#productDetailsCarousel > div.owl-stage-outer > div > div.owl-item.active > a > picture > img")
        except NoSuchElementException:
        	print("Exception Handled")
        	continue
        ```
        

---

**Veri çekerken selenium ile beutifulSoap karışık kullandık. BeutifulSoap’da veri çekememe problemi seleniuma göre daha çok oldu.**

### Web Scraping Kullanılan Kütüphaneler

```python
#BeautifulSoup
from bs4 import BeautifulSoup
import requests

#Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#Kontrol
import validators
```

### Selenium Kütüphanesi

1. Google üzerinden arama yaptırma
    
    ```python
    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")
    Veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    Veri_girisi.send_keys("Aranılacak veri")
    Veri_girisi.send_keys(Keys.ENTER)
    ```
    
2. İlgili sayfaya yönlendirme
    
    ```python
    # xpath gibi aramalar da yapılabilir
    tikla = browser.find_element("css selector","ilgili sayfanın linkinin olduğu yerin selector kopyası")
    tikla.click()
    ```
    
3. Fotograf indirme *(Projenin güncel halinde bu özelliğe gerek kalmadı, isteğe bağlı kullanılabilir)*
    
    ```python
    img_url = browser.find_element("XXXXXXX").get_attribute("src")
    browser.get(img_url)
    img_loc = "C:/Users/zerha/Downloads/xxxx.png"
    browser.save_screenshot(img_loc)
    ```
    
4. Veri Çekme
    
    ```python
    product_price = browser.find_element("css selector","#pdp-main > div.pdp-block2.pdpGeneralWidth > div.pdp-details > div.addtocart-component > div > div.AddToCart-AddToCartAction > div > div.pdp-amount.prc-last-2 > div > div > span")
    product_priceText = product_price.get_attribute("innerHTML")
    ```
    

### BeautifulSoap Kütüphanesi

1. Veri çekme
    
    ```python
    response = requests.get(base_url.format(i), headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('li',{'class': 'productListContent-zAP0Y5msy8OHn5z7T_K_'})
    ```
    

## Veritabanı

Web sitelerinden veri çekerken ilk önce request ile web sitelerine giriş yaptık. Daha sonrasında aldığımız response değerler 200’ü gösterdiğini teyit edince response içerisindeki html bilgileri kullanarak request attığımız site içindeki verileri çektik. Çektiğimiz verileri direkt olarak mongoDb’ye kaydettik.

Kullandığımız varlıkların(entitys) temel özellikleri: 

- Bilgisayar:
    - Fotoğrafı
    - Marka Model
    - Adı
    - Model No İşletim sistemi
    - İşlemci tipi
    - İşlemci nesli
    - Ram Disk boyutu
    - Disk türü
    - Ekran boyutu
    - Puanı
    - Fiyat
    - Bu bilgilerin alındığı site/siteler
- User(Admin):
    - Kullanıcı adı
    - Şifresi

Scraping ile çekilen bilgiler düzenli olarak veritabanında ve sitede güncellenmektedir. 

Önceden kayıtlı olan bir verinin tekrardan kaydının önlenmesi için Duplicate kontrolü yapılmaktadır. Aynı zamanda Near Duplicate kontrolü ile aynı ürün bilgilerinin farklı isimlendirmelere tekrarlanmaması sağlanır. 

### Neden MongoDB Kullandık?

Semi-structured, json tipinde veriler varsa ve bu verilerin herhangi bir yerinde sorgulama, groupby gibi işlemler gerekiyorsa Doküman tabanlı (Document- Oriented) NoSQL veritabanları seçilir. MongoDB doküman tabanlı NoSql veritabanlarından biridir. Peki özellikle bu tür veritabanlarından MongoDB veritabanını seçtik?

Çünkü MongoDB’nin çokça kendine ait nasıl kullanılacağını anlatan kaynaklara sahip. Diğer Doküman tabanlı NoSQL veritabanlarına göre daha çok kullanılıyor.Bu da proje geliştirirken daha kolay ilerlememizi sağladı.

![Screenshot 2022-10-09 161909.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/Screenshot_2022-10-09_161909.png)

MongoDB, verileri kaydettiği dokumanları JSON benzeri Binary JSON (BSN) formatında saklar. MongoDB’de yaptığımız işlemlerin ilişkisel veritabanındaki karşılıkları:

---

### MongoDb Veritabanı Oluşturma

MongoDb de yapılan işlemler:

1. Yeni bir Cluster oluşturuldu. İsmi: "Cluster-WebScraping"
2. Cluster-WebScraping için veritabanı erişim izni verilen iki kullanıcı oluşturuldu.
    - isim: zeyneperhan şifre: 20012022
    - isim: hazarkoc şifre:20012022
3. Cluster-WebScraping'e IP üzerinden otomatik bağlanmak için Ip adresi eklendi
    
    > **Not: *Colab Notebook*** üzerinden denemeler yaptığımız için IP hatası almamak adına “Allow Acces From Anywhere” özelliğini seçtik.
    > 
4. Cluster içerisine yeni veritabanı eklenip koleksiyon oluşturuldu.

### MongoDb Bağlantısını Oluşturma

```python
# MongoDb işlemleri için gerekli kütüphaneler eklendi
import pymongo
```

Cluster-WebScraping Url’sini elde etmek için:

1. MongoDb Atlas veya MongoDb Compass'a göre seçim yapılır.
    - MongoDb Atlas'ı seçtiğimiz için MongoDB Drivers kısmı seçilir.
2. Driver ve versiyonu seçilir.
    - Driver: Pyhton Versiyon: 3.4 ve sonrası
        
        > **NOT:** Burada verdiği linki direkt kopyalamamak gerekiyor! Direkt olarak verdiği link içerisinde admin veritabanı bağlantısı içeriyor ama bu Mongo Atlas üzerinden görünmüyor. Bu yüzden Compas kullanmasak bile url’yi istediğimiz şekilde ayarlamak için Compas’ı kullandık.
        > 

```python
# Cluster-WebScraping için bağlantı sağlandı (Compass yardımı ile). (username: zeyneperhan password: 20012022)
myclient = pymongo.MongoClient("mongodb://zeynep:20012022@ac-akv12vk-shard-00-00.6erqfem.mongodb.net:27017,ac-akv12vk-shard-00-01.6erqfem.mongodb.net:27017,ac-akv12vk-shard-00-02.6erqfem.mongodb.net:27017/?ssl=true&replicaSet=atlas-8ffx15-shard-0&retryWrites=true&w=majority") 

# Kullanacağımız veritabanı için erişim sağladık.
mydb = myclient["Bilgisayar"]

# Bilgisayar Veritabanındaki Amazon koleksiyonuna erişim sağladık
mycollectionAmazon= mydb["Amazon"]
```

### MongoDb CRUD İşlemleri

1. **CREATE**
    
    ```python
    mycollection.insert_one(XXXX)
    ```
    
2. **READ**
    1. Koleksiyon İçerisindeki Verileri okuma
    
    ```python
    # mycollection içerisindeki verileri teker teker alıp ilgili özelliği yazdırır.
    for product in mycollection.find({}):
      print(product['Name'])
    ```
    
    b. Koleksiyon içerisindeki verinin **gömülü dokümantasyon** bilgilerini okuma:
    
    ```python
    for product in mycollection.find({}):
      print("----------------")
      print(product['Name'])
      print("\n")
    
      hepsiburada = product['HepsiBurada']
    
      print("HepsiBurada Bilgileri:")
      print(hepsiburada['URL'])
      print(hepsiburada['Price'])
    
      print("\n")
      trendyol = product['Trendyol']
    
      print("Trendyol Bilgileri:")
      print(trendyol['URL'])
      print(trendyol['Price'])
      print("----------------")
    ```
    
    ***Çıktısı:*** 
    
    ![MongoDb Verilerine Erişme 1.png](README%20md%2012bb0b63b45b4f7b9dfdfea4a5f15e33/MongoDb_Verilerine_Erime_1.png)
    
3. **UPDATE**
    1. Verinin içerisinde **gömülü dokümantasyonu** güncelleme:
    
    ```python
    #Name bilgisi product['Name'] olan verinin Trendyol Objesinin içerisindeki URL bilgisini günceller
    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"Trendyol.URL": "yeni bilgi"}})
    ```
    
4. **DELETE**

### MongoDb Sorgulama İşlemleri

1. ***Filtreleme***
    
    **ObjectId:**
    
    ```python
    # ObjectId sorgulaması yapmak işçin gerekli kütüphane
    from bson.objectid import ObjectId
    product = mycollection.find_one({"_id": ObjectId('Aranan verinin idsi')})
    
    # İlgili verinin ObjectId değerini çekmek için:
    id = product['_id']
    ```
    

## WebScraping ve MongoDB Algoritması

> **NOT:** Google CAPTCHA’dan kurtulmak User Agent’ı sürekli değiştirmek veya insan davranışlarına daha uygun olacak şekilde time.sleep() komutu kullanmak faydalı olabiliyor.
> 

### Başka Kullanım şekilleri

Aslında bu algoritmayı şu şekilde uyarlayabilirsiniz:

1. Şimdiki halinde olduğu bir belli bir eticaret sitesinin bilgisayar sayfalarını baz alıp diğer sitelerden fiyat bilgileri çekerek çalışma.
2. Elinizde bulunan bilgisayar isimlerini(bu isimler model,marka,seri no, ram gibi detaylı bilgiler bulundurmalı) diğer sitelerde aratarak veri ekleme.
3. Sırayla sitelerin hepsinden model ismi alarak.
    
    <aside>
    🚨 NOT: MongoDb içerisinde verilerin duplicate olmasını engellemek adına:
    
    </aside>
    
    1. Örenğin ilk olarak hepsiburadadan Bilgisayar isimleri, ilgili bilgisayarın fotoğrafı ve detaylı biligsini çekip elimizde bulunan **7 web sitesi**(hepsiburada,amazon,trendyol,n11,çiçeksepeti,vatan,teknosa) için arama yaptıralım.
    2. bittikten sonra amazondan bilgisayar isimleri, ilgili bilgisayarın fotoğrafı ve detaylı biligsini çekip elimizde bulunan **6 web** sitesi(amazon,trendyol,n11,çiçeksepeti,vatan,teknosa) için arama yaptıralım.
        1. Bu aşamada mongodb içerisinde kayıtlı verilerde amazon.mevcut bilgisi true olanla amazondan çekilen bilgileri karşılaştırılmalı. çakışma olursa bu veri atlanıp diğer veriye geçilmeli.
    3. gibi gibi bu şekilde azaltılarak devam ettirilebilir.

```python
def hepsiBuradaTam():

    mycollection.delete_many({})
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}

    # Verileri çekeceğimiz sitenin ana url'si
    base_url = 'https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98?sayfa={0}'

    #veriyi tutan dict
    item = {}
    j=0
    for i in range(3,4):
        
        print('Processing {0}...'.format(base_url.format(i)))
        print("-------------")  
        time.sleep(0.50)  

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
            item["index"] = j
            j=j+1
            try:
                product_url = 'https://www.hepsiburada.com'+result.a.get("href")
                valid=validators.url(product_url)
                if valid==True:
                    
                    product_response = requests.get(product_url, headers=headers)
                    product_soup = BeautifulSoup(product_response.content, 'html.parser')
                    product_details = product_soup.find_all("table",{"class":"data-list tech-spec"})
                    detail={}
                    browser = webdriver.Chrome(driver_path)
                    time.sleep(0.50)
                    browser.get(product_url)
                    try:
                        Marka = browser.find_element("css selector","body > div.wrapper > main > div.product-detail-module > section.detail-main > div.container.contain-lg-4.contain-md-4.contain-sm-1.fluid > div > div.productDetailRight.col.lg-2.md-2.sm-1.grid-demo-fluid > div.product-information.col.lg-5.sm-1 > span > a").get_attribute("innerHTML")
                        detail["Marka"]= Marka
                    except NoSuchElementException:
                        print("Exception Handled")
                        continue
                    for details in product_details:

                        informations = details.find_all("tr")

                        for info in informations:

                            try:               
                                label = info.find("th").text
                                label=label.replace(" ", "")
                                value = info.find("span").text
                                detail[label]=value
                                
                            except AttributeError:
                                continue
                    item["Details"]=detail
                    try:
                        time.sleep(0.50)
                        img_url = browser.find_element("css selector","#productDetailsCarousel > div.owl-stage-outer > div > div.owl-item.active > a > picture > img").get_attribute("src")
                        item["Img"]= img_url
                    except NoSuchElementException:
                        print("Exception Handled")
                        continue
                    time.sleep(0.50)
                    browser.close()
                else:
                    print("Invalid url")
                    print(product_url)
                    continue    

                
            except AttributeError:
                continue

            item["Name"] = product_name

            mycollection.insert_one(item)
            item.clear()
```

```python
def cicekSepetiExtra(product):
    
    mycollection.update_one({ "Name" : product['Name'] },{ "$set": {"cicekSepetiExtra.Mevcut": False}})
    name = product['Name']
    time.sleep(0.50)
    browser = webdriver.Chrome(driver_path)
    browser.get("https://www.google.com/")
    time.sleep(0.50)

    cicekSepetiExtra_veri_girisi = browser.find_element("css selector",".gLFyf.gsfi")
    time.sleep(0.50)
    cicekSepetiExtra_veri_girisi.send_keys(name+" "+" site:ciceksepeti.com")
    time.sleep(0.50)
    cicekSepetiExtra_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(0.50)
    try:
        cicekSepetiExtra_tikla = browser.find_element("css selector","#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e.VGXe8 > div > a")
        time.sleep(0.50)
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
    time.sleep(0.50)
    browser.close()
```

## Kaynakça

1. BTK AKADEMİ: Talha Kılıç
    
    [NoSQL - Doküman Veritabanları](https://www.btkakademi.gov.tr/portal/course/nosql-dokueman-veritabanlari-21625)
    
2. Slider 
    
    [How to Create a Range Slider Using HTML & CSS?](https://uxplanet.org/how-to-create-a-range-slider-using-html-css-6112fe9346e4)
    
3. W3Schools Template
    
    [W3Schools online HTML editor](https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_clothing_store&stacked=h)
    
4. MongoDB Crud & Connection
    
    [ASP.NET Core with MongoDB || Complete CRUD || MongoDB Compass || NoSQL || .NET 5.0](https://www.youtube.com/watch?v=dsvL22_w88I)
    
5. Checkbox 
    
    [How To Create a Custom Checkbox and Radio Buttons](https://www.w3schools.com/howto/howto_css_custom_checkbox.asp)
    
    [Implementing Checkbox Product Filters ASP.NET MVC - How Can I Pass Data in Collection through URL?](https://stackoverflow.com/questions/42283295/implementing-checkbox-product-filters-asp-net-mvc-how-can-i-pass-data-in-colle)
    
    [Checkbox Filter asp.net mvc| Applying Filters using Checkbox on Shop Page in ASP.Net MVC- Session 21](https://www.youtube.com/watch?v=I8ZZsXEeLxs)
    
6. Pyton json formatında yazdırma
    
    [Pandas to_json: How to export DataFrame to JSON File](https://appdividend.com/2022/03/15/pandas-to_json/#:~:text=To%20convert%20the%20object%20to,use%20the%20to_json()%20function)
    
7. Pyhton with MongoDb
    
    [Python MongoDB](https://www.w3schools.com/python/python_mongodb_getstarted.asp)
    
8. Selenium ile web scraping
    
    [Web Scraping with Selenium in Python - Amazon Search Result(Part 1)](https://medium.com/@jb.ranchana/web-scraping-with-selenium-in-python-amazon-search-result-part-1-f09c88090932)
    
9. MongoDb dizi ve gömülü dokümanlar ile çalışmak
    
    [https://www.mongodb.com/docs/manual/core/document/](https://www.mongodb.com/docs/manual/core/document/)
    
10. MongoDb gömülü doküman güncellemek için
    
    [$inc](https://www.mongodb.com/docs/v4.2/reference/operator/update/inc/?_ga=2.133247691.497944246.1666347531-498109847.1665859348)
    
11. Selenium hata döndürme
    
    [How To Handle Errors And Exceptions In Selenium Python | LambdaTest](https://www.lambdatest.com/blog/handling-errors-and-exceptions-in-selenium-python/)
    
12. Filtreleme işlemleri
    
    [Django E-commerce Product Filter Prototype](https://www.youtube.com/watch?v=uDw7ArEVYSY)
    
    [Django Filtering System Using Django-Filter | Django Filtering Tutorial](https://www.youtube.com/watch?v=TTeNn3kNWD8)
    
13. Admin Paneline Buton Eklenmesi

[django-admin-extra-buttons](https://pypi.org/project/django-admin-extra-buttons/)