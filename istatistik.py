import pandas as pd
import numpy as np
basliklar= ['sira','dunki_sira','film_adi','gunluk_kazanc','gunluk_brut_degisim','haftalik_brut_degisim','salon_sayisi','ort','su_gunekadar','gun','dagitici','tarih']
df = pd.read_csv('2000-2020-DailyDataBoxOfficeNew.csv', sep='*', names= basliklar)


#Datamızı başta excel için ayarladığımız için ve böyle bir imkan varken tekrar çekmemek için düzeltmeler yapıyoruz.

df['gunluk_kazanc'] = df['gunluk_kazanc'].str.replace(',','',regex=True)

df['gunluk_brut_degisim'] = df['gunluk_brut_degisim'].str.replace(',','.',regex=True)

df['gunluk_brut_degisim'] = df['gunluk_brut_degisim'].str.replace('%','',regex=True)

df['haftalik_brut_degisim'] = df['haftalik_brut_degisim'].str.replace(',','.',regex=True)

df['haftalik_brut_degisim'] = df['haftalik_brut_degisim'].str.replace('%','',regex=True)

df['salon_sayisi'] = df['salon_sayisi'].str.replace(',','',regex=True)

df['ort'] = df['ort'].str.replace(',','',regex=True)

df['su_gunekadar'] = df['su_gunekadar'].str.replace(',','',regex=True)

df['gun'] = df['gun'].str.replace(',','',regex=True)

#Veri tipi dönüşümlerini yapıyoruz.

df['sira'] = df['sira'].astype(float)

df['dunki_sira'] = df['dunki_sira'].astype(float)

df['gunluk_kazanc'] = df['gunluk_kazanc'].astype(float)

df['salon_sayisi'] = df['salon_sayisi'].astype(float)

df['ort'] = df['ort'].astype(float)

df['su_gunekadar'] = df['su_gunekadar'].astype(float)

df['gun'] = df['gun'].astype(float)

#Burada 2000-2020(dahil değil) yılları arası başlayıp ve son bulan filmleri elde tutuyoruz

baslayanlar_1 = df[df['gun'] == 1] # tüm data içindeki tüm filmlerin sadece ilk gününcü satırlarını aldım

baslayanlar_1 = baslayanlar_1[baslayanlar_1['tarih'].str[2:4] != '20'] #bunlardan 2020 yılında ilk günü olan satırları çıkarttım

son_data = pd.DataFrame()

for i in baslayanlar_1['film_adi']: #elimizde olan 2000-2019(dahil) yılları arasında başlangıç günü bulunan filmleri isimleri aracılığı ile dolaşacağız
	film_adi = df[df['film_adi'] == i] #daraltılmamış olan df datamızdan o filmin tüm satırlarını çekiyoruz
	max_deger = film_adi['gun'].max() # ilk günü belli olan filmlerin kaçıncı günde bittiği bilgisni int olarak alıyoruz
	max_gunlu_film = film_adi[film_adi['gun'] == max_deger]	#2 satır üstteki anadatadan aldığımız tüm filmlerden bu sefer son günlerini alıyoruz
	sonuc = max_gunlu_film['tarih'].str[2:4] == '20' # son günleri tanımlı olan datamızdan 2020 tarihli olanları seçiyoruz
	if(sonuc.max() == True): #eğer seçili film 2020 tarihinde bitiyorsa if bloğuna girer
		baslayanlar_1 = baslayanlar_1.drop(baslayanlar_1[baslayanlar_1['film_adi']==i].index) # ve o filmi datamızdan atarız

#burada başlangıç günü ve bitiş günü 2000-2019(dahil) yılları arasında olan filmleri almış olduk sadece (datamızı küçülttük)
#elimizdeki baslayanlar_1 datası sadece filmlerin ilk günlerinin sütunlarını tutuyor
#bazı filmler aynı adla tekrar gösterime girmiş veya aynı adı içeriyor, onları tekrar elememiz gerekiyor


film_list = baslayanlar_1['film_adi'].to_list()
istatistik_data = df[df['tarih'].str[2:4] != '20']
istatistik_data = istatistik_data[istatistik_data['film_adi'].apply(lambda i: i in film_list)]

deneme19 = istatistik_data[istatistik_data['tarih'].str[2:4] == '19']
deneme20 = df[df['tarih'].str[2:4] == "20"]

film_adlari_list19 = list((deneme19['film_adi'].value_counts().to_dict().keys()))
film_adlari_list20 = list((deneme20['film_adi'].value_counts().to_dict().keys()))

for i in film_adlari_list19:
    if(i in film_adlari_list20):
        istatistik_data = istatistik_data.drop(istatistik_data[(istatistik_data['film_adi']==i) & (istatistik_data['tarih'].str[2:4]=='19')].index)
#Yukarıdaki işlemler sonucunda datamız istatistik için hazırdır  

#istatistik_data[istatistik_data['dagitici']=='Paramount Pictures']['su_gunekadar'].sum()
tum_film_adlari = list((istatistik_data['film_adi'].value_counts().to_dict().keys()))
t_f_max_satirlar = [istatistik_data[istatistik_data['su_gunekadar']==istatistik_data[istatistik_data['film_adi']==i]['su_gunekadar'].max()] for i in tum_film_adlari]

max_indexler = [a.index[0] for a in t_f_max_satirlar]

data_max = istatistik_data[istatistik_data.index.to_series().apply(lambda i : i in max_indexler)] #7dk sürdü

tum_dagitici_adlari = list((data_max['dagitici'].value_counts().to_dict().keys()))

yil_20_toplamgelir = data_max['su_gunekadar'].sum()
yillik_20_dagitici_gelirleri ={}
for i in tum_dagitici_adlari:
    yillik_20_dagitici_gelirleri.update({i:data_max[data_max['dagitici'] == i]['su_gunekadar'].sum()})
 
ilk_10_list =sorted(yillik_20_dagitici_gelirleri.values())[-10:]
new_dict = {}
for i in yillik_20_dagitici_gelirleri:
    if(yillik_20_dagitici_gelirleri[i] in ilk_10_list):
        new_dict.update({i:yillik_20_dagitici_gelirleri[i]})

kalan = 100
for i in new_dict:
    print(i,': %'+str(new_dict[i]/(yil_20_toplamgelir/100)))
    kalan = kalan -new_dict[i]/(yil_20_toplamgelir/100)
print('Kalan şirketler : %'+str(kalan))