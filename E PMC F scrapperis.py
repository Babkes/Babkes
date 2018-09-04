import pandas as pd
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time
import random
pagrindas = r'https://europepmc.org/Funders/'
base_url='https://europepmc.org/search?'
driver_path=r'C:\Users\g.rozenaite\Desktop\chromedriver.exe'
urls = []
pages = []
df = pd.DataFrame([])
# gaunu urls
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(pagrindas)
result1 = driver.page_source
soup1 = BeautifulSoup(result1, 'lxml')
moneta = soup1.find_all("a",  {"class": "boldlink"})
for m in moneta:
    m = m.get('href')
    urls = urls.append(m)
    print (urls)
# gaunu naujus url
for u in urls:
    next_link =soup.findAll("a", {"class": "nextLink"})
    crap,new=next_link[0]['href'].split('?')
    go_to=base_url+new
    pages.append()  
#%% apsibrezti funkcija, kuri leistu surasti pid+pmcid ir tada atskirti 
    
#%% action - gaunu id
driver.get('https://www.google.com/')
time.sleep(10)
n=1
for p in pages:
    try:
        print('Processing: ', p)
        n = n + 1
        driver.get(p)
        result = driver.page_source
        text, links = process_data(result)
        print (text)
        df = df.append(pd.DataFrame(
        {'url': [p],
         #'article': []
         'PMID': [pmid],
         'PMCID': [pmcid]}
        index=[0]), ignore_index=True)
    except:
driver.close()
