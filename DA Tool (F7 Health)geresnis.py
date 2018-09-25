import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
import random
import pyodbc
names_df = pd.read_excel(r'C:\Users\VPVI\Desktop\Neliesti\Pradzia.xlsx'
                         , sheet_name = 'Adagio')
galutinis_exc = pd.ExcelWriter(r'C:\Users\VPVI\Desktop\Neliesti\Galutinis produktas.xlsx')
names = names_df['name'].values.tolist()
url_df = pd.DataFrame([])
text_df = pd.DataFrame([])
api_key = "AIzaSyAp3TRE8lc3A02rf0X82tRckIcx8pPosFc"
cse_id = "007703736530656354066:0q3s49bgw44"
driver_path=r'C:\Users\VPVI\Desktop\Neliesti\chromedriver.exe' 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=PPMI-28-NB\QSRNVIVO10;"
                      "Database=MEDIA;"
                      "Trusted_Connection=yes;")
 
cursor = cnxn.cursor()
'''
cursor.execute("""
CREATE TABLE Media_results
(id int IDENTITY(1,1) PRIMARY KEY,
company_id int NOT NULL,
comapny_name_O varchar(max) NOT NULL,
company_name varchar(max) NOT NULL,
site_url varchar(max) NOT NULL,
snippet text,
text text NULL,
extraction_date datetime NOT NULL DEFAULT CURRENT_TIMESTAMP)
""")
'''
cnxn.commit()

#%%
def google_search(search_term, api_key, cse_id, **kwargs):
    search = build("customsearch", "v1", developerKey=api_key)
    results = search.cse().list(q = search_term, cx=cse_id, lr='lang_en', **kwargs).execute()
    if ('items') in results:
        return results ['items'] 
    else:
        print (n + ' ' + 'No Results')
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
    soup = clean_it(soup)
    text = soup.text
    text = mini_clean(text)
    return(text)
#%%seaching
miss = ['Anton Proksch Institut','ALIMENTARY HEALTH ', 'NATIONAL CENTER FOR SCIENTIFIC AND TECHNOLOGICAL RESEARCH * INSTITUTE FOR RESEARCH IN HEALTH SCIENCES']
ni = 701
for n in names[701:900]:
    time.sleep(3)
    print (ni, '/', len(names))
    ni = ni + 1
    try:
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
    except HttpError:
        miss.append(n)
        print ('No luck')
        pass

#%%merging
galutinis_df = pd.merge(names_df [['id', 'raw_name','name']],
                        url_df[['snippet', 'name', 'url']],
                 on=['name'], 
                 how='inner')
for i, row in galutinis_df.iterrows():
    sql = (row['id'], row['raw_name'], row['name'], row['url'], row['snippet'])
    query="INSERT INTO Media_results(company_id, comapny_name_O, company_name, site_url, snippet) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, sql)
    cnxn.commit()
#%%
other_url = [r'https://medcitynews.com/2015/04/healthcare-business-intelligence-april-10-2015/',
             r'https://www.news-medical.net/news/20100608/Gene-variant-linked-to-ability-of-Tibetans-to-cope-with-low-oxygen-conditions-identified.aspx',
             r'https://www.healio.com/endocrinology/obesity/news/online/%7Bfb011ffb-ad47-48d2-afed-38a7af7a6fce%7D/scientists-re-create-brain-neurons-to-study-obesity',
             r'https://medcitynews.com/2016/05/startup-health-finalnd-identifies-5-health-tech-startups/',
             r'https://www.medicalnewstoday.com/categories/neurology',
             r'https://www.healthcare-informatics.com/content/healthcare-informatics-executive-exchange-registration']
time_url = [r'https://www.news-medical.net/sitemaps/category/Medical-Condition-News.aspx',
            r'https://www.healio.com/hematology-oncology/news/headlines?startItem=2020&Filter=',
            r'https://www.healthcaredive.com/news/new-statewide-health-organization-forming-in-arizona/280181/',
            r'https://www.healio.com/orthopedics/journals/ortho/1987-8-10-8/%7B97797480-3509-494d-9c8d-83592a80480b%7D/calendar-of-events.pdf',
            r'https://www.healio.com/pediatrics/practice-management/news/online/%7B3ea96fa6-eae2-42f7-a41e-a241957a8dc4%7D/exposure-to-veterinary-drugs-most-common-in-younger-children',
            r'https://medcitynews.com/2018/09/federal-appeals-court-rules-for-mit-harvard-in-crispr-patent-case/?rf=1',
            r'https://medcitynews.com/2010/01/illinois-biotech-advocacy-group-elects-adm-executive-as-chairman/',
            r'https://www.mpo-mag.com/contents/view_breaking-news/2015-01-30/biotronik-to-offer-new-treatment-options-with-release-of-orsiro-drug-eluting-stent',
            r'https://www.healthcare-informatics.com/news-item/mobile/cedars-sinai-offer-apple-watch-app',
            r'https://medicalxpress.com/news/2016-09-surgeons-trial-smart-glasses-mid-op.html',
            r'https://www.mpo-mag.com/contents/view_breaking-news/2016-12-20/stimguard-enrolls-first-patient-in-office-based-chronic-tibial-nerve-oab-study',
            r'https://www.mpo-mag.com/heaps/view/500/page_6/113970']
urls = galutinis_df['url'].values.tolist()
for us in urls:
    if us in time_url:
        urls.remove(us)
for us in urls:
    if 'sitemap' in us:
        urls.remove(us)

driver = webdriver.Chrome(driver_path)
ui = 1
random.shuffle(urls)
driver.get('https://www.google.com/')
for u in urls:
    print('Processing: ', u)
    print(ui, '/', len(urls))
    ui = ui + 1
    time.sleep(5)
    try:
        driver.get(u)
        driver.set_page_load_timeout(40)
        result = driver.page_source
        text = process_data(result)
        print (text)
        text_df = text_df.append(pd.DataFrame({'url': [u], 'text': [text]}, 
                         index = [0]), ignore_index = True)
    except Exception as e: 
        if e == 'TimeoutException':
            print ('Time is money!')
            time_url.append(u)
            driver.get('https://www.google.com/')
            pass
        else: 
            print("¯\_(ツ)_/¯")
            driver.get('https://www.google.com/')
            other_url.append(u)
            pass 
driver.close()
#%%saving
galutinis_df = pd.merge(galutinis_df[['id', 'raw_name', 'name', 'url', 'snippet']], text_df[['url', 'text']],
                        on = ['url'], how = 'left')
galutinis_df.to_excel(galutinis_exc, 'Pabaiga')
galutinis_exc.save()
#%%
galutinis_df.to_csv(r'C:\Users\VPVI\Desktop\Neliesti\Galutinis produktas.csv')
#%%
for i, row in galutinis_df.iterrows():
    sql = (row['id'], row['raw_name'], row['name'], row['url'], row['snippet'], row['text'])
    query="INSERT INTO Media_resultssies(company_id, comapny_name_O, company_name, site_url, snippet, text) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(query, sql)
    cnxn.commit()
