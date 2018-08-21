import pandas as pd
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time
import random
url_df = pd.read_excel(r"C:\Users\g.rozenaite\Desktop\Link galutinio produkto.xlsx",
                       sheet_name='Testuojam gramdyma')
urls = url_df['url'].values.tolist()
text_df = pd.DataFrame([])
driver_path=r'C:\Users\g.rozenaite\Desktop\\chromedriver.exe' 
#Defining data collection, crawling, and cleaning functions
def get_links_from_soup(soup):
	links = [ item.get('src') for item in soup.find_all('frame') ]
	links = [ l for l in links if l is not None]
	return list(set(links))
#
def clean_it(soup):
	try:
		for script in soup.find_all('script'):
			gb = script.extract()
	except:
		None
	try:
		for script in soup.find_all('div',{'id':'toolbar'}):
			gb = script.extract()
	except:
		None
	try:
		for script in soup.find_all('style'):
			gb = script.extract()
	except:
		None
	try:
		gb = soup.find('table').find('tbody').find('tr').extract()
	except:
		None
	try:
		gb = soup.find('div', {'id': 'gallerypageheader'}).extract()
	except:
		None
	try:
		gb = soup.find('div', {'id': 'header'}).extract()
	except:
		None
	try:
		gb = soup.find('div', {'id': 'footer'}).extract()
	except:
		None
	try:
		gb = soup.find('div', {'id': 'secondary'}).extract()
	except:
		None
	try:
		gb = soup.find('div', {'id': 'sidebar'}).extract()
	except:
		None
	try:
		gb = soup.find('div', {'id': 'footerbarwrap'}).extract()
	except:
		None
	try:
		gb = soup.find('div', {'id': 'mainpageheader'}).extract()
	except:
		None
	try:
		gb = soup.find('ul', {'id': 'help_box_history'}).extract()
	except:
		None
	try:
		gb = soup.find('div', {'id': 'box_contact_qr'}).extract()
	except:
		None
	try:
		gb = soup.find('div', {'class': 'wrapper_secondary'}).extract()
	except:
		None
	try:
		gb = soup.find('title').extract()
	except:
		None
	return (soup)
#
def mini_clean(string):
	string2=re.sub('\n\n+', '\n\n', string)
	string2=re.sub('\t\t+', '\t', string2)    
	string2=string2.replace('\xa0', '\t')
	string2=string2.replace('\xad', '\t')
	string2=string2.replace(r'\n\s*\n', r'\n\n') 
	return(string2)
#
def process_data(result):
	soup = BeautifulSoup(result, 'lxml')
	links = get_links_from_soup(soup)
	soup = clean_it(soup)
	text = soup.text
	text = mini_clean(text)
	return(text, links)
#%%
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.google.com/')
time.sleep(10)
n=1
#random.shuffle(urls)
for u in urls: #[5001:8000]:
    try:
        print('Processing: ', u)
        print(n, '/', len(urls))
        n = n + 1
        driver.get(u)
        result = driver.page_source
        text, links=process_data(result)
        text_df = text_df.append(pd.DataFrame(
        {'url': [u],
         'text': [text]},
        index=[0]), ignore_index=True)
        print(text)
    except:
        None
driver.close()
#%%
galutinis_df = pd.merge(url_df[['snippet', 'id', 'url']],
						  text_df[['url', 'text']],
                          on=['url'],
                          how='left')
galutinis_exc = pd.ExcelWriter(r"C:\Users\g.rozenaite\Desktop\Galutinis produktas.xlsx")
galutinis_df.to_excel(galutinis_exc, 'Pabaiga')
galutinis_exc.save()