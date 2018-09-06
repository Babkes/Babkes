import pandas as pd
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time
names_df = pd.read_excel(r"C:\Users\g.rozenaite\Desktop\Link galutinio produkto.xlsx"
                         , sheet_name = 'Testuojam pabaiga')
galutinis_exc = pd.ExcelWriter(r"C:\Users\g.rozenaite\Desktop\Galutinis produktas.xlsx")
names = names_df['name'].values.tolist()
url_df = pd.DataFrame([])
text_box = []
api_key = "AIzaSyB9KBuW01lIrnk8PoIbyntZAdpQkB4iD54"
cse_id = "007703736530656354066:2sgdezn3w2e"
driver_path=r'C:\Users\g.rozenaite\Desktop\\chromedriver.exe' 
#%%
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    results = service.cse().list(q = search_term, cx=cse_id, **kwargs).execute()
    if ('items') in results:
        return results ['items'] 
    else:
        print (n + ' ' + 'No Results')
#
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
    try:
        gb = soup.find('div', {'class': 'user-menu'}).extract()
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
#%%seaching
time.sleep(10)
for n in names:
    results1 = google_search(n, api_key, cse_id, num=10)
    if results1 != None:
        for result in results1:
            url_df = url_df.append(pd.DataFrame(
                    {'name': [n], 'url': [result['link']], 
                     'snippet': [result['snippet']]},
                    index=[0]), ignore_index=True)
    results2 = google_search(n, api_key, cse_id, num=10, start = 11)
    if results2 != None:
        for result in results2:
            url_df = url_df.append(pd.DataFrame(
                    {'name': [n], 'url': [result['link']], 
                     'snippet': [result['snippet']]},
                    index=[0]), ignore_index=True)
#%%merging
galutinis_df = pd.merge(names_df [['id','name']],
                        url_df[['snippet', 'name', 'url']],
                 on=['name'], 
                 how='left')
urls = galutinis_df['url'].values.tolist()
#%%parsing
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.google.com/')
time.sleep(10)
n=1
for u in urls:
    try:
        print('Processing: ', u)
        print(n, '/', len(urls))
        n = n + 1
        driver.get(u)
        result = driver.page_source
        text, links=process_data(result)
        print (text)
        text_box.append(text)
        galutinis_df ['text'] = text_box
    except:
        print (' ¯\_(ツ)_/¯')
driver.close()
#%%saving
galutinis_df.to_excel(galutinis_exc, 'Pabaiga')
galutinis_exc.save()