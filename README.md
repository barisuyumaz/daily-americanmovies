# daily-americanmovies
To capture and analyze daily data of American films that were released in the USA between 2000-2020.

Kurulumu ve Kullanımı
Öncelikle daily-00-20.py kaydedilecek adrese kendi bilgisayarınızın adresini ekleyip, gerekli kütüphaneleri bilgisayara yükleyip bu py dosyasını çalıştırıyoruz. 
Takribi 5-6 saat içinde 2000 yılından 2020 yılının sonuna kadar günlük tüm film verilerini çekiyor.
İstatistik çıkarmadan önce istatistik.py dosyasının içinde datamızı 2000-2020 yılları içinde ilk ve son gösterimi yapılmış filmleri seçerek daraltıyoruz.
İstatistik çıkarılmaya hazır hale geldikten sonra ilk elde ettiğimiz bilgi, en çok kazanan 10 dağıtımcı şirketin 20 yıl içindeki pazardaki ortalama payları ne kadardır?
Sorusunun cevabıdır.
---
Warner Bros. : %15.958506965628056
Universal Pictures : %12.71277470350712
Twentieth Century Fox : %11.416016733985238
Lionsgate : %4.788386734461975
Walt Disney Studios Motion Pictures : %16.975391093799274
Sony Pictures Entertainment (SPE) : %9.312163068664887
Paramount Pictures : %7.7714814561342385
New Line Cinema : %1.9587535338499213
DreamWorks Distribution : %1.6901578686640508
DreamWorks : %2.537006128745428
Kalan şirketler : %14.879361712559803
---
Daha fazla istatistik için devamı gelecek...

#Instructions

##Before running daily-00-20.py file:
###1. Make sure all required libaries have installed
```python
import requests
from bs4 import BeautifulSoup
import csv
import datetime
import time
```
check it: 1. run 'pip freeze' in cmd and check 2. execute import 'requires lib' and if you don't get error, keep move)
###2. Define a path on line 29 for your .csv file to be created 
