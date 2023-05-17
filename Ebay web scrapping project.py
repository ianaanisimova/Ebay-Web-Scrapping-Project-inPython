#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[51]:


# Connect to Website 

URL = 'https://www.ebay.ca/itm/403989074166?hash=item5e0fa010f6:g:fmoAAOSwhipjbgsH&amdata=enc%3AAQAIAAAA4OjGohqDDngJcONlUltIgb4KPyubHQFTOdPDVRVg5u877xtKwgnjVTQd%2FM2S65a3lDSEwkuRldzjbroLa%2FToFnrSbygS9omj%2BMMVi7tHuEbr1ufL6dsL3W9WrB7uRJdnfgRKx8rkE7GU%2B4uC3VKCfGzRdWZfYcoTom%2BRyA%2FGuao1EQQBS%2BJkGMvSYv9%2BWxnXrF5mVAYCd8TK2qxNJyXUHPhMxAi%2BhZF2ZLkuexVJD%2Fa6SMCx%2BVJTGRldAVYSPzseY5gCSoucaOSiwZuRc0QIY%2F%2BmDlDE57%2FIut%2FmsAOgFCDd%7Ctkp%3ABk9SR9aoi9CEYg'

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(),"html.parser" )

title = soup2.find( id ='vi-lkhdr-itmTitl').get_text()

price = soup2.find(itemprop = "price").get_text()


print(title)
print(price)





# In[52]:


price = price.strip()[4:]
title = title.strip()

print(title)
print(price)


# In[53]:


import datetime 

today = datetime.date.today()

print(today)


# In[55]:


import csv

header = ['Title', 'Price', 'Date']
data = [title, price, today]

with open('EbayWebScrDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[63]:


import pandas as pd

df = pd.read_csv(r'C:\Users\ianaa\anaconda3\EbayWebScrDataset.csv')

print(df)


# In[62]:


#Appending data to the csv

with open('EbayWebScrDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[64]:


def check_price():
    URL = 'https://www.ebay.ca/itm/403989074166?hash=item5e0fa010f6:g:fmoAAOSwhipjbgsH&amdata=enc%3AAQAIAAAA4OjGohqDDngJcONlUltIgb4KPyubHQFTOdPDVRVg5u877xtKwgnjVTQd%2FM2S65a3lDSEwkuRldzjbroLa%2FToFnrSbygS9omj%2BMMVi7tHuEbr1ufL6dsL3W9WrB7uRJdnfgRKx8rkE7GU%2B4uC3VKCfGzRdWZfYcoTom%2BRyA%2FGuao1EQQBS%2BJkGMvSYv9%2BWxnXrF5mVAYCd8TK2qxNJyXUHPhMxAi%2BhZF2ZLkuexVJD%2Fa6SMCx%2BVJTGRldAVYSPzseY5gCSoucaOSiwZuRc0QIY%2F%2BmDlDE57%2FIut%2FmsAOgFCDd%7Ctkp%3ABk9SR9aoi9CEYg'
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"}
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(),"html.parser" )
    title = soup2.find( id ='vi-lkhdr-itmTitl').get_text()
    price = soup2.find(itemprop = "price").get_text()
    price = price.strip()[4:]
    title = title.strip()
    import datetime 
    today = datetime.date.today()
    
    import csv
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]
    with open('EbayWebScrDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        



# In[ ]:


while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd

df = pd.read_csv(r'C:\Users\ianaa\anaconda3\EbayWebScrDataset.csv')

print(df)


# In[ ]:




