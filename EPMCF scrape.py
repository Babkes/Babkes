import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time
pagrindas = [r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Academy+of+Medical+Sciences%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Action+on+Hearing+Loss%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Alzheimer%27s+Society%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Arthritis+Research+UK%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Austrian+Science+Fund+FWF%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Biotechnology+and+Biological+Sciences+Research+Council%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Bloodwise%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Breast+Cancer+Now%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22British+Heart+Foundation%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Cancer+Research+UK%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Chief+Scientist+Office%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Diabetes+UK%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22The+Dunhill+Medical+Trust%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22European+Research+Council%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Marie+Curie%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Medical+Research+Council%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Motor+Neurone+Disease+Association%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Multiple+Sclerosis+Society%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Myrovlytis+Trust%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22National+Centre+for+the+Replacement,+Refinement+and+Reduction+of+Animals+in+Research%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Department+of+Health+and+Social+Care%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Parkinson%27s+UK%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Prostate+Cancer+UK%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Swiss+National+Science+Foundation%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Telethon%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Wellcome+Trust%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Wellcome+Trust-DBT+India+Alliance%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22World+Health+Organization%22+AND+SRC:med',
             r'https://europepmc.org/search;jsessionid=4B106C608B6E3B10F1397FA525DA66D9?page=1&query=grant_agency:%22Worldwide+Cancer+Research%22+AND+SRC:med']
base_url = 'https://europepmc.org/search?'
driver_path= r'C:\Users\VPVI\Desktop\Neliesti\chromedriver.exe'
galutinis_exc = pd.ExcelWriter(r'C:\Users\VPVI\Desktop\Neliesti\EPMCF.xlsx')
df = pd.DataFrame([])
driver = webdriver.Chrome(driver_path)
time.sleep(5)
for p in pagrindas:
    driver.get(p)
    result1 = driver.page_source
    soup1 = BeautifulSoup(result1, 'lxml')
    p_pages = soup1.findAll("a", {"class": "nextLink"})
    if len(p_pages) == 0:
        print (p + '  ' + 'Fin')
        pass
    else:
        crap,page = p_pages[0]['href'].split('?')
        pages = base_url + page
        pagrindas.append(pages)
for p in pagrindas:
    driver.get(p)
    result2 = driver.page_source
    soup2 = BeautifulSoup(result2, 'lxml')
    yda = soup2.find_all('span', {'class': 'pmid'})
    for i in yda:
        text = i.text
        crap, text = text.split('(PMID:')
        if ' ' in text:
            pmid, pmcid = text.split(' ')
            crap, pmcid = pmcid.split('PMCID:')
            pmcid, crap = pmcid.split (')')
        else:
            pmid, crap = text.split(')')
            pmcid = 'None'
        df = df.append(pd.DataFrame({'PMID': [pmid], 'PMCID': [pmcid]}, index = [0]),
                       ignore_index = True)
driver.close()
df.to_excel(galutinis_exc, 'Pabaiga')
galutinis_exc.save()