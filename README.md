# Daily Datas of American Movies and Their Gross in Domestic Theaters
## Python Web Scrapping
## Instructions

### Before running daily-00-20.py file:

#### 1. Make sure all required libaries have installed
```python
import requests
from bs4 import BeautifulSoup
import csv
import datetime
import time
```
check it: 1. run 'pip freeze' in cmd and check || 2. execute import 'required lib' and if you don't get error, keep move)

#### 2. Define a path which speacial for you computer on line 29 for your .csv file to be created 

### Run daily-00-20.py

#### How it works?
* Merging string date variable(for example: '2000/12/31') and the main link('https://www.boxofficemojo.com/date/')
* Through the 'requests' lib, we pull the html source codes of specified link.
* Convert raw html source data to a tidy form and reach the searched data with 'bs4' lib.
* Edit your data with Python string methods.
* Export your organized data into specified file(.csv)

#### It will take around 5-6 hours after run daily-00-20.py file.

### Run istatistik.py file:
To get statistical results
#### How it works?
* Firstly, it narrows the datas to get statistics between exactly 20 years.
* Then, get results according to our questions.
#### Example Question: What are the top 10 most profitable distributors between 2000 and 2020 and what is their percentage in the American Market?

* Warner Bros. : %15.958506965628056
* Universal Pictures : %12.71277470350712
* Twentieth Century Fox : %11.416016733985238
* Lionsgate : %4.788386734461975
* Walt Disney Studios Motion Pictures : %16.975391093799274
* Sony Pictures Entertainment (SPE) : %9.312163068664887
* Paramount Pictures : %7.7714814561342385
* New Line Cinema : %1.9587535338499213
* DreamWorks Distribution : %1.6901578686640508
* DreamWorks : %2.537006128745428
* Rest Distributor Companies : %14.879361712559803
