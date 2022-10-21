# .Net Core ile Web Scraping E-Ticaret

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
3. Siteden çekilen verinin özelliklerinin None olup olmaması

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

![Screenshot 2022-10-09 161909.png](https://github.com/zeynepaslierhan/KOU-WebScraping-YazLab1/blob/main/img/Neden%20MongoDB%20Kulland%C4%B1k%201.png)

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
