import requests
from bs4 import BeautifulSoup
import csv
import datetime
import time

#LİNKLER----------
url_value1 = 'https://www.boxofficemojo.com/date/'

dt = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2020, 12, 31)
step = datetime.timedelta(days=1)

result = []

while dt < end:
    result.append(dt.strftime('%Y-%m-%d'))
    dt += step
#------------------------------------------

baslangic = time.time()
with open('C:/Users/Administrator/Desktop/bitirme projesi/2000-2020-DailyDataBoxOffice.csv','w',newline='') as dosya:
	for k in range(len(result)): 
		try:
			icerik = requests.get("https://www.boxofficemojo.com/date/"+result[k]+"/").content

			soup = BeautifulSoup(icerik,"html.parser")


			yeni = soup.find_all("div",{"class":"a-section imdb-scroll-table-inner"})[0]

			pekyeni = yeni.find_all("tr")[1:] # Burada başlık satırından kurtuluyoruz

			thewriter = csv.writer(dosya, delimiter="*")
			for i in range(len(pekyeni)): #kaç tane satır varsa o kadar döndürüyor
				epeyyeni = pekyeni[i].find_all("td")
				writelist = []
				for j in range(11): #satırın içinde dönüyor
					if(epeyyeni[:11][j].text == "-"):
						veri = ""
					elif(j == 2):
						veri = epeyyeni[:11][j].text.replace("\n","")
					elif(j == 10):
						 veri = epeyyeni[:11][j].text.replace("\n","")
					else:
						veri = epeyyeni[:11][j].text.replace("\n","").replace("$","").replace(".",",")
					writelist.append(veri)
				writelist.append(result[k])
				thewriter.writerow(writelist)
		except:
			pass
	dosya.close()

print(time.time()-baslangic)

