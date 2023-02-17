import requests
from bs4 import BeautifulSoup
import csv
import datetime
import time

#LINK----------
url_value1 = 'https://www.boxofficemojo.com/date/'

#DATES---------
dt = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2020, 12, 31)
step = datetime.timedelta(days=1)

result = []

while dt < end:
    result.append(dt.strftime('%Y-%m-%d'))
    dt += step
#--------------

#MEASURING TIME
start = time.time()
#-------------

#MAIN---------
with open('C:/Users/baris/Desktop/american-theaters-project/2000-2020-DailyDataBoxOffice.csv','w',newline='') as dosya:
	for k in range(len(result)): 
		try:
			r = requests.get("https://www.boxofficemojo.com/date/"+result[k]+"/").content

			soup = BeautifulSoup(r,"html.parser")

			hmltdata = soup.find_all("div",{"class":"a-section imdb-scroll-table-inner"})[0]

			newdata = hmltdata.find_all("tr")[1:] # we get rid off heading row here

			thewriter = csv.writer(dosya, delimiter="*")
			for i in range(len(newdata)): #returns how many row it has
				lastdata = newdata[i].find_all("td")
				writelist = []
				for j in range(11):
					if(lastdata[:11][j].text == "-"):
						data = ""
					elif(j == 2):
						data = lastdata[:11][j].text.replace("\n","")
					elif(j == 10):
						 data = lastdata[:11][j].text.replace("\n","")
					else:
						data = lastdata[:11][j].text.replace("\n","").replace("$","").replace(".",",")
					writelist.append(data)
				writelist.append(result[k])
				thewriter.writerow(writelist)
		except:
			pass
	dosya.close()
#-------------

print(time.time()-start)#prints how long it took since you run this program

