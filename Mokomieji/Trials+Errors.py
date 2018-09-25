from bs4 import BeautifulSoup
import requests
import openpyxl
from googleapiclient.discovery import build
r = requests.get('')
soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.findAll('tr', {"class": "upcoming_performance"})
"Scraping"
def google_scrape(url):
    thepage = urllib.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text
i = 1
query = 'search this'
for url in search(query, stop=10):
    a = google_scrape(url)
    print (url)
    print (" ")
    i += 1   
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())
r = requests.get('')
soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.findAll('tr', {"class": "upcoming_performance"})
r = requests.get('')
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')
for s in soup.find_all(id="rhs_block"):
        print(s.text)
print(cellObj.value)
com = openpyxl.load_workbook('Health F7.xlsx')
sheet = com.get_sheet_by_name('Imones')            
for i in range ():
    if i in ID:
        print(ID.cell(row=i, column=2).value)
    else:
        print ("Hi")
        df1.join(df2,on=name,how='right')
#%% 
names_df = pd.read_excel('Galutinis produktas.xlsx', sheet_name = 'Testuojam paieska')
keywords = {'AARHUS UNIVERSITET', 'AYMING', 'UNIVERSITAET STUTTGART'}
api_key = "AIzaSyB9KBuW01lIrnk8PoIbyntZAdpQkB4iD54"
cse_id = "007703736530656354066:2sgdezn3w2e"
def google_search(keywords, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        results = service.cse().list(q = keywords, cx=cse_id, **kwargs).execute()
        if ('items') in results:
            return results ['items'] 
        else:
            print ('No Results, maybe next time!')
for i in keywords:
    results = google_search(i, api_key, cse_id, num=1)
    if results != None:
        for result in results:
            print (i + '    ' + result['formattedUrl'])
#%%
import requests

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
response = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
text_box = soup.find('body')
text = text_box.text.strip()
f = open('obo-t17800628-33.html', 'w')
f.write(text)
f.close
#%%
from bs4 import BeautifulSoup
import requests

url = r'https://scrapethissite.com/pages/simple/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print (soup)
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
text_box = clean_it(soup)
text = text_box.text.strip()
print (text_box)
#%% parse url
def get_links_from_soup(soup):
	links = [ item.get('src') for item in soup.find_all('frame') ]
	for item in soup.find_all('a'):
		if 'href' in item.attrs:
			link_content = item.get('href')
			if not any(bad in link_content for bad in bad_segments):
				links.append(link_content)
	links = [ l for l in links if l is not None]
	return list(set(links))
#%% saving text
from bs4 import BeautifulSoup
import requests
url = r'https://www.news-medical.net/sitemaps/category/Medical-Condition-News.aspx'
thepage = requests.get(url)
soup = BeautifulSoup(thepage, "html.parser")
print (thepage)
print (soup)

#%%
mergerisdf = pd.merge(url_df [['id','url']],
                text_df[['url', 'text']],
                 on=['name'], 
                 how='left')   
mergerisexc = pd.ExcelWriter('Galutinis produktas.xlsx')
mergerisdf.to_excel(mergerisexc, 'Pradzia')
mergerisexc.save()
#%%
from BeautifulSoup import BeautifulSoup, Comment
import re, htmlentitydefs
from HTMLParser import HTMLParseError
from datetime import datetime
import subprocess
import os
import urllib2

def safe_html(html):
    if not html:
        return None
    # remove these tags, complete with contents.
    blacklist = ["script", "style" ]
    whitelist = [
        "div", "span", "p", "br", "pre",
        "table", "tbody", "thead", "tr", "td", "a",
        "blockquote",
        "ul", "li", "ol",
        "b", "em", "i", "strong", "u", "font"
        ]
    try:
        # BeautifulSoup is catching out-of-order and unclosed tags, so markup
        # can't leak out of comments and break the rest of the page.
        soup = BeautifulSoup(html)
    except HTMLParseError, e:
        # special handling?
        raise e

    # now strip HTML we don't like.
    for tag in soup.findAll():
        if tag.name.lower() in blacklist:
            # blacklisted tags are removed in their entirety
            tag.extract()
        elif tag.name.lower() in whitelist:
            # tag is allowed. Make sure all the attributes are allowed.
            tag.attrs = [(a[0], safe_css(a[0], a[1])) for a in tag.attrs if _attr_name_whitelisted(a[0])]
        else:
            # not a whitelisted tag. I'd like to remove it from the tree
            # and replace it with its children. But that's hard. It's much
            # easier to just replace it with an empty span tag.
            tag.name = "span"
            tag.attrs = []

    # scripts can be executed from comments in some cases
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    for comment in comments:
        comment.extract()
    safe_html = unicode(soup)
    if safe_html == ", -":
        return None
    return safe_html
def _attr_name_whitelisted(attr_name):
    return attr_name.lower() in ["href", "style", "color", "size", "bgcolor", "border"]
def safe_css(attr, css):
    if attr == "style":
        return re.sub("(width|height):[^;]+;", "", css)
    return css
def plaintext(input):
    """Converts HTML to plaintext, preserving whitespace."""
    # from http://effbot.org/zone/re-sub.htm#unescape-html
    def _unescape(text):
        def fixup(m):
            text = m.group(0)
            if text[:2] == "&#":
                # character reference
                try:
                    if text[:3] == "&#x":
                        return unichr(int(text[3:-1], 16))
                    else:
                        return unichr(int(text[2:-1]))
                except ValueError:
                    pass
            else:
                # named entity
                try:
                    text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
                except KeyError:
                    pass
            return text # leave as is
        return re.sub("&#?\w+;", fixup, text)
    input = safe_html(input) # basic sanitation first
    text = "".join(BeautifulSoup("<body>%s</body>" % input).body(text=True))
    text = text.replace("xml version='1.0' encoding='%SOUP-ENCODING%'", "") # strip BS meta-data
    return _unescape(text)
#%%
    def text (sc_text):
    text = re.search()
    return (sc_text)
    text = re.search((name))
    url_df = url_df.append(pd.DataFrame(
                    {'text': text}, index=[0]), ignore_index=True)
    print(url_df)
#%%
import pandas as pd
import pickle
df = pd.read_excel(r"C:\Users\g.rozenaite\Desktop\Pradzia.xlsx"
                         , sheet_name = 'Adagio')
list1 = df['name'].values.tolist()
list2 = df['ForNER'].values.tolist()
dict = dict(zip(list1, list2))
file = open (r"C:\Users\g.rozenaite\Desktop\name_dict.pkl", 'wb')
pickle.dump(dict, file)
file.close()
#%%
import requests
from bs4 import BeautifulSoup
import re

url = "https://www.15min.lt/"
response = requests.get(url)
page = str(BeautifulSoup(response.content, 'lxml'))
def getURL(page):
    start_link = page.find("href=")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    muki = page[start_quote + 1: end_quote]
    return muki, end_quote
mylist = [] #gaunam kruva linku
while True:
    for u in url:
        muki, n = getURL(page)
        page = page[n:]
        if url:
            mylist.insert(0, url)
        else:
            break      
twitter = re.compile(r'https://twitter.com/(.*)')
handles = []
interim = []
for item in mylist:
    findings = twitter.search(item)
    interim.append(findings)

for i in interim: 
    if i is not None: 
         handles.append(i.group())
    else: 
        pass

print(handles)
#%%
import pandas as pd
import re
import string
mano_df = pd.read_excel(r'C:\Users\g.rozenaite\Documents\Darbai\Viskas su DATA\Viskas su Publications\Book3_Done.xlsx',
                       sheet_name = 'Sheet2')
isbn = mano_df['isbn'].to_string()
for i in isbn:
    i = re.sub(r'[^\w]', ' ', i)
    print (isbn)
#%%
malada = soup1.findAll("span", {"class": 
           "results_listcitation_title citation-title"})
for m in malada:
    title = m.text     
#%%
import pandas as pd
import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=vpvi-77-pc\sqlexpress;"
                      "Database=TutorialDB;"
                      "Trusted_Connection=yes;")
 
cursor = cnxn.cursor()
'''
cursor.execute("""
CREATE TABLE EPMCF
(id int IDENTITY(1,1) PRIMARY KEY,
site_url varchar(max) NOT NULL,
PMID int NOT NULL,
PMCID varchar(max),
Funder text)
""")
'''
cnxn.commit()

#df1 = pd.read_excel(r'C:\Users\g.rozenaite\Desktop\EPMCF.ranknis.xlsx')
df2 = pd.read_csv(r'C:\Users\g.rozenaite\Desktop\EPMCF.a.csv')
#df3 = pd.concat([df1, df2], ignore_index = True)
'''
df3['funder'] = pd.np.where(df.URL.str.contains('%22Academy+of+Medical+Sciences%22'), 'Academy of Medical Sciences'
   pd.np.where(df.URL.str.contains('Action+on+Hearing+Loss'), 'Action on Hearing Loss',
   pd.np.where(df.URL.str.contains('%22Alzheimer%27s+Society%22'), 'Alzheimer"s Society',
   pd.np.where(df.URL.str.contains('%22Arthritis+Research+UK%22'), 'Arthritis Research UK',
   pd.np.where(df.URL.str.contains('%22Austrian+Science+Fund+FWF%22'), 'Austrian Science Fund FWF',
   pd.np.where(df.URL.str.contains('%22Biotechnology+and+Biological+Sciences+Research+Council%22'),'Biotechnology and Biological Sciences Research Council',
   pd.np.where(df.URL.str.contains('%22Bloodwise%22'), 'Bloodwise',
   pd.np.where(df.URL.str.contains('%22Breast+Cancer+Now%22'), 'Breast Cancer Now',
   pd.np.where(df.URL.str.contains('%22British+Heart+Foundation%22'), 'British Heart Foundation',
   pd.np.where(df.URL.str.contains('%22Cancer+Research+UK%22'), 'Cancer Research UK',
   pd.np.where(df.URL.str.contains('%22Chief+Scientist+Office%22'), 'Chief Scientist Office',
   pd.np.where(df.URL.str.contains('%22Diabetes+UK%22'), 'Diabetes UK',
   pd.np.where(df.URL.str.contains('%22The+Dunhill+Medical+Trust%22'), 'The Dunhill Medical Trust',
   pd.np.where(df.URL.str.contains('%22European+Research+Council%22'), 'European Research Council',
   pd.np.where(df.URL.str.contains('%22Marie+Curie%22'), 'Marie Curie',
   pd.np.where(df.URL.str.contains('%22Medical+Research+Council%22'), 'Medical Research Council',
   pd.np.where(df.URL.str.contains('%22Motor+Neurone+Disease+Association%22'), 'Motor Neurone Disease Association',
   pd.np.where(df.URL.str.contains('%22Multiple+Sclerosis+Society%22'), 'Multiple Sclerosis Society',
   pd.np.where(df.URL.str.contains('%22Myrovlytis+Trust%22'), 'Myrovlytis Trust',
   pd.np.where(df.URL.str.contains('%22National+Centre+for+the+Replacement,+Refinement+and+Reduction+of+Animals+in+Research%22'), 'National Centre for the Replacement, Refinement and Reduction of Animals in Research',
   pd.np.where(df.URL.str.contains('%22Department+of+Health+and+Social+Care%22'), 'Department of Health and Social Care',
   pd.np.where(df.URL.str.contains('%22Parkinson%27s+UK%22'),'Parkinson"s UK',
   pd.np.where(df.URL.str.contains('%22Prostate+Cancer+UK%22'), 'Prostate Cancer UK',
   pd.np.where(df.URL.str.contains('%22Swiss+National+Science+Foundation%22'), 'Swiss National Science Foundation',
   pd.np.where(df.URL.str.contains('%22Telethon%22'), 'Telethon',
   pd.np.where(df.URL.str.contains('%22Wellcome+Trust%22'), 'Wellcome Trust',
   pd.np.where(df.URL.str.contains('%22Wellcome+Trust-DBT+India+Alliance%22'), 'Wellcome Trust-DBT India Alliance',
   pd.np.where(df.URL.str.contains('%22World+Health+Organization%22'), 'World Health Organization',
   pd.np.where(df.URL.str.contains('%22Worldwide+Cancer+Research%22'), 'Worldwide Cancer Research', 'Other')))))))))))))))))))))))))))))

df3 = df3[df3['funder'].str.contains('%22Academy+of+Medical+Sciences%22').replace())]
'''
for i, row in df2.iterrows():
    sql = (row['URL'], row['PMID'], row['PMCID'])
    query="INSERT INTO EPMCF(site_url, PMID, PMCID) VALUES (?, ?, ?)"
    cursor.execute(query, sql)
    cnxn.commit()
#%%
import pandas as pd
import pyodbc
df= pd.read_excel(r'C:\Users\g.rozenaite\Desktop\Pradzia.xlsx')
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=vpvi-77-pc\sqlexpress;"
                      "Database=MEDIA;"
                      "Trusted_Connection=yes;")
 
cursor = cnxn.cursor()
cnxn.commit()
for i, row in df.iterrows():
    sql = (row['projectRcn'], row['projectID'], row['id'], row['raw_name'], row['name'], row['ForNER'])
    query="INSERT INTO Pradzia(projectRcn, ProjectID, company_id, comapny_name_O, company_name, forNER) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(query, sql)
    cnxn.commit()
#%%LogReg
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
reggies = cross_val_score(LogisticRegression(), x_t, y_z, cv = 5)
print (np.mean(reggies))
#%% market
for i, row in df_texts.iterrows():
    doc = nlp(row[-1])
    for token_t in doc:
        for i in m_zodynas:
            if token_t.text == i:
                list.append(i)
    if len(list) != 0:
        print (list)
        print (row[1])
        df_dict = df_dict.append(pd.DataFrame(
        {'company_id': [row[1]], 'site_url': [row[2]], 'Market stage': [len(list)]},
        index=[0]), ignore_index=True)
    else:
        print ('No matches found')
        df_dict = df_dict.append(pd.DataFrame(
        {'company_id': [row[1]], 'site_url': [row[2]], 'Market stage': [0]},
        index=[0]), ignore_index=True)
#%% 
from sklearn.feature_extraction.text import CountVectorizer        
vect_pre_m = CountVectorizer().fit(pre_m_zodynas)
y_pre_m = vect_pre_m.transform(pre_m_zodynas)
print(vect_pre_m.vocabulary_)
text = nlp(pre_m_zodynas)
for token in text:
    print (token, token.pos_)
for n in nace:
    vect_n = CountVectorizer().fit(n)
    y_n = vect_n.transform(n)
    print(vect_n.vocabulary_)
    text = nlp(n)
    for token in text:
        print (token, token.pos_)
n = 1
for t in texts:
    ti = [t]
    vect_t = CountVectorizer(stop_words = stop).fit(ti)
    x_t = vect_t.transform(ti)
    #feature_names = vect_t.get_feature_names()
    print (n)
    print(vect_t.vocabulary_)
    n = n + 1
    text = nlp(t)
    for token in text:
        print (token, token.pos_)
#%%
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

cnxn.commit()
#%%
import spacy
nlp = spacy.load('en')
doc = nlp('ores, ore')
for i in doc:
    print (i.text, i.lemma_)
#%%
import pandas as pd
json = pd.read_csv(r'C:\Users\g.rozenaite\Desktop\D4I_company_summary.csv')
json = json.reset_index()
json = json.drop('index', 1)
#%%
mama = [['http://www.cytos.com/press-release', 'http://www.cytos.com/news/274/105/Kuros-appoints-Philippe-Saudan-as-Chief-Development-Officer.html', 'http://www.cytos.com/news/273/105/valuationLAB-Initiates-Research-Coverage-on-Kuros.html', 'http://www.cytos.com/news/275/105/Arbutus-terminates-license-agreement-for-VLP-platform-for-the-treat-ment-of-hepatitis-B-infections.html', 'http://www.eurice.eu/news/2017/06/28/new-research-project-nomad-increases-nuclear-power-plant-safety/', 'http://www.eurice.eu/news/2015/10/15/the-official-programme-of-the-seurat-1-symposium-now-available/', 'https://www.presens.de/company.html', 'https://www.presens.de/company/news/artikel/new-optical-oxygen-probe-for-bioreactors-136.html', 'https://www.presens.de/industries/food-beverage.html', 'https://www.presens.de/knowledge.html', 'https://www.presens.de/industries/industry-technical.html', 'https://www.presens.de/support-services/certificates.html', 'https://www.presens.de/support-services/shipping-instructions.html', 'https://www.presens.de/product-finder/5rsp6qh6ngrovvsurlg4u7ds9u.html', 'https://www.presens.de/oemcustom/our-offer.html', 'https://www.presens.de/support-services/kla-calculator.html', 'https://www.presens.de/support-services/faqs.html', 'https://www.presens.de/newsletter.html', 'https://www.presens.de/company/meet-us.html', 'https://www.presens.de/industries/biology-environmental.html', 'https://www.presens.de/company/press.html', 'https://www.presens.de/industries/biotech-pharma.html', 'https://www.presens.de/oemcustom/production.html', 'https://www.presens.de/company/news.html', 'https://www.presens.de/oemcustom.html', 'https://www.presens.de/support-services/presens-newsletter.html', 'https://www.presens.de/industries/medical-life-sciences.html', 'https://www.presens.de/legal-info.html', 'https://www.presens.de/company/news/artikel/facilitate-calibrating-of-co2-sensor-foils-140.html', 'https://www.presens.de/company/news/artikel/gathering-speed-presens-at-the-company-run-2017-135.html', 'https://www.presens.de/support-services/faqs/question/can-i-use-the-sg-1-silicone-glue-for-the-visisens-co2-sensor-foils-also-292.html', 'https://www.presens.de/support-services/faqs/question/how-do-i-start-the-oxy-flux-1208.html', 'https://www.presens.de/support-services/faqs/question/i-have-more-than-one-sdr-connected-can-i-choose-which-sdrs-i-want-to-use-for-measurement-239.html', 'https://www.presens.de/support-services/faqs/question/why-does-my-ph-sensor-not-work-in-tap-water-49.html', 'https://www.presens.de/support-services/faqs/question/where-do-i-need-sensor-spot-sizes-different-from-the-common-diameter-of-5-mm-approx-02-inch-85.html', 'https://www.presens.de/support-services/faqs/question/which-microorganisms-have-already-been-tested-for-biomass-measurement-with-the-sfr-vario-and-in-whi.html', 'https://www.presens.de/support-services/faqs/question/can-i-use-the-manual-micromanipulator-with-an-implantable-microsensor-as-well-or-is-it-only-for-nee.html', 'https://www.presens.de/support-services/faqs/question/why-are-there-two-different-calibration-data-sets-for-sensordishesr-547.html', 'https://www.presens.de/support-services/faqs/question/can-the-visisens-co2-sensor-foils-also-be-used-in-the-gas-phase-330.html', 'https://www.presens.de/support-services/faqs/question/how-far-does-the-metal-tip-of-the-temperature-sensor-have-to-be-immersed-in-the-medium-to-give-accur.html', 'https://www.presens.de/support-services/faqs/question/which-glue-can-i-use-to-integrate-optical-sensor-spots-23.html', 'https://www.presens.de/support-services/faqs/question/your-pictures-show-clamps-for-your-shake-flasks-sfs-can-i-also-work-with-sticky-mats-83.html', 'https://www.presens.de/support-services/faqs/question/can-i-use-the-sdr-with-other-formats-than-the-24-well-plates-65.html', 'https://www.presens.de/support-services/faqs/question/the-standard-size-of-the-visisens-sensor-foils-is-rectangle-4-x-4-cm-what-can-i-do-if-my-sample-re.html', 'https://www.presens.de/support-services/faqs/question/which-toxicity-tests-where-done-with-the-sensordishr-63.html', 'https://www.presens.de/knowledge/basics/detail/kla-determination-in-shake-flasks-1067.html', 'https://www.presens.de/support-services/faqs/question/the-sdr-software-shows-no-sensor-instead-of-a-value-what-is-the-reason-241.html', 'https://www.presens.de/support-services/faqs/question/why-does-the-sdr-software-show-ph.html', 'https://www.presens.de/support-services/faqs/question/how-can-i-prepare-the-calibration-solutions-cal0-and-cal100-for-oxygen-sensors-35.html', 'https://www.presens.de/support-services/faqs/question/how-can-i-perform-online-co2-measurements-with-the-sfr-vario-are-there-flasks-with-alrea.html', 'https://www.presens.de/support-services/faqs/question/i-forgot-my-sfrs-password-user-name-what-can-i-do-to-access-the-software-again-526.html', 'https://www.presens.de/support-services/faqs/question/what-factors-will-affect-the-oxygen-reading-37.html', 'https://www.presens.de/support-services/faqs/question/which-substances-can-interfere-with-the-optical-o2-ph-and-co2-measurements-1.html', 'https://www.presens.de/support-services/faqs/question/can-i-save-trend-arithmetic-calculations-done-in-the-sdr-software-can-i-do-them-for-all-channels.html', 'https://www.presens.de/support-services/faqs/question/why-do-i-need-to-equilibrate-my-samples-for-such-long-time-periods-before-measurement-with-the-sdr.html', 'https://www.presens.de/support-services/faqs/question/how-can-i-convert-an-oxygen-value-into-a-different-oxygen-unit-121.html', 'https://www.presens.de/support-services/faqs/question/what-is-the-correct-way-for-handling-an-oxygen-or-ph-microsensor-1104.html', 'https://www.presens.de/support-services/faqs/question/does-each-oxygen-sensor-spot-need-a-separate-calibration-or-are-the-calibration-values-valid-for-th.html', 'https://www.presens.de/support-services/faqs/question/do-i-measure-co2-or-hco3-57.html', 'https://www.presens.de/support-services/faqs/question/can-the-customer-integrate-the-optical-sensor-spots-by-himself-herself-77.html', 'https://www.presens.de/support-services/faqs/question/i-am-using-sfr-sfr-vario-what-is-the-difference-between-sfs-v3-and-sfs-v4-1068.html', 'https://www.presens.de/support-services/faqs/question/what-is-the-difference-between-user-defined-calibration-and-one-point-adjustment-for-the-sdr-when-d.html', 'https://www.presens.de/support-services/faqs/question/how-often-will-i-have-to-exchange-the-microsensor-474.html', 'https://www.presens.de/support-services/faqs/question/can-i-integrate-an-oxygen-microsensor-into-a-catheter-97.html', 'https://www.presens.de/support-services/faqs/question/i-formerly-used-the-oxygen-biosensor-obs-from-bd-can-i-use-the-oxoplate-as-a-substitute-257.html', 'https://www.presens.de/support-services/faqs/question/the-presens-datamanager-measurement-studio-software-cannot-connect-to-the-fibox-4-device-what-can.html', 'https://www.presens.de/support-services/faqs/question/what-is-the-maximum-flow-rate-and-pressure-for-your-oxygen-flow-through-cells-472.html', 'https://www.presens.de/support-services/faqs/question/can-i-re-use-the-shake-flasks-with-integrated-sensors-79.html', 'https://www.presens.de/support-services/faqs/question/is-the-glue-or-the-sensor-spot-biocompatible-which-tests-were-done-are-there-any-studies-on-leach.html', 'https://www.presens.de/support-services/faqs/question/which-buffers-can-be-used-for-calibration-of-chemical-optical-ph-sensors-222.html', 'https://www.presens.de/support-services/faqs/question/can-the-manual-micromanipulator-get-wet-and-be-used-under-water-484.html', 'https://www.presens.de/support-services/faqs/question/how-to-prepare-buffers-of-constant-ionic-strength-and-calibrate-optical-ph-sensors-47.html', 'https://www.presens.de/support-services/faqs/question/are-there-any-constraints-when-autoclaving-glass-or-plastic-vessels-with-integrated-self-adhesive-ph.html', 'https://www.presens.de/support-services/faqs/question/what-is-the-minimum-sensor-size-for-visisens-280.html', 'https://www.presens.de/support-services/faqs/question/is-my-microplate-reader-compatible-to-the-sensor-plates-71.html', 'https://www.presens.de/support-services/faqs/question/which-side-of-the-visisens-sensor-foils-has-to-face-the-sample-119.html', 'https://www.presens.de/support-services/faqs/question/can-i-use-the-sdr-for-measurement-of-photosynthesis-567.html', 'https://www.presens.de/support-services/faqs/question/i-try-to-investigate-oxygen-consumption-in-my-cell-culture-however-the-oxygen-level-stays-at-100.html', 'https://www.presens.de/support-services/faqs/question/are-the-fluorescence-intensities-i-get-from-the-sensor-plate-with-my-reader-sufficient-for-a-good-me.html', 'https://www.presens.de/support-services/faqs/question/what-cannula-steel-needle-sizes-are-available-for-profiling-microsensors-993.html', 'https://www.presens.de/support-services/faqs/question/what-is-salinity-what-value-should-i-enter-in-the-sdr-software-541.html', 'https://www.presens.de/support-services/faqs/question/are-the-oxygen-sensors-used-with-fibox-3-lcd-trace-and-microx-tx3-trace-compatible-with-microx.html', 'https://www.presens.de/support-services/faqs/question/can-the-profiling-microsensor-be-used-with-the-microx-tx3-trace-1062.html', 'https://www.presens.de/support-services/faqs/question/how-does-temperature-affect-the-oxygen-measurement-105.html', 'https://www.presens.de/support-services/faqs/question/can-i-re-use-the-sensordishesr-235.html', 'https://www.presens.de/support-services/faqs/question/the-pt100-temperature-sensor-delivered-with-my-presens-meter-is-too-large-for-my-measurement-set-up.html', 'https://www.presens.de/support-services/faqs/question/there-are-jumps-in-my-visisens-time-series-what-can-i-do-304.html', 'https://www.presens.de/support-services/faqs/question/how-do-i-verify-whether-the-oxygen-sensor-is-giving-correct-readings-performance-proof-5.html', 'https://www.presens.de/support-services/faqs/question/what-are-the-response-times-for-the-oxygen-sensors-based-on-the-2-mm-fiber-like-non-invasive-oxygen.html', 'https://www.presens.de/support-services/faqs/question/is-the-sfr-vario-measuring-od-optical-density-466.html', 'https://www.presens.de/support-services/faqs/question/how-can-i-install-the-sfrs-on-a-pc-with-windows-10-1185.html', 'https://www.presens.de/support-services/faqs/question/i-cannot-log-into-the-sfr-software-sfrs-from-my-windows-account-what-can-i-do-413.html', 'https://www.presens.de/support-services/faqs/question/what-is-the-maximum-resolution-of-visisens-a1-can-we-see-up-to-micro-scale-274.html', 'https://www.presens.de/support-services/faqs/question/what-is-the-smallest-tip-size-available-for-profiling-microsensors-995.html', 'https://www.presens.de/support-services/faqs/question/in-which-vessel-can-i-integrate-a-sensor-spot-99.html', 'https://www.presens.de/support-services/faqs/question/why-are-the-fluorescence-intensities-and-ratios-i-get-with-my-reader-different-from-the-ones-in-the.html', 'https://www.presens.de/knowledge/basics/detail/oxygen-uptake-rate-our-calculation-1066.html', 'https://www.presens.de/support-services/faqs/question/why-do-i-see-peaks-in-the-graphs-of-the-sdr-software-especially-in-the-oxygen-signal-when-i-open-t.html', 'https://www.presens.de/support-services/faqs/question/what-is-the-operating-principle-of-the-co2-sensor-51.html', 'https://www.presens.de/support-services/faqs/question/can-the-sfr-vario-be-used-for-biomass-monitoring-in-mammalian-or-insect-cell-culture-494.html', 'https://www.presens.de/support-services/faqs/question/how-can-i-do-a-biomass-calibration-with-the-sfr-vario-can-i-calibrate-only-for-od-measurement-528.html', 'https://www.presens.de/support-services/faqs/question/the-sdr-software-says-no-sdr-found-what-can-i-do-551.html', 'https://www.presens.de/support-services/faqs/question/can-the-same-meter-be-used-for-ph-oxygen-or-co2-sensors-1.html', 'https://www.presens.de/support-services/faqs/question/when-should-i-calibrate-my-oxy-flux-eco-pst7-microsensor-1212.html', 'https://www.presens.de/support-services/faqs/question/the-sfr-software-sfrs-cannot-connect-to-the-device-what-can-i-do-411.html', 'https://www.presens.de/support-services/faqs/question/can-i-use-a-different-measurement-interval-for-each-connected-sdr-243.html', 'https://www.presens.de/knowledge/basics/detail/the-stern-volmer-relationship-900.html', 'https://www.presens.de/support-services/faqs/question/what-is-the-measurement-angle-and-how-is-it-determined-994.html', 'https://www.presens.de/support-services/faqs/question/do-cells-grow-on-the-sensor-inside-the-sensordishesr-67.html', 'https://www.presens.de/support-services/faqs/question/can-the-profiling-microsensor-be-submerged-in-water-992.html', 'https://www.presens.de/support-services/faqs/question/do-the-sensors-work-in-turbid-solutions-15.html', 'https://www.presens.de/support-services/faqs/question/what-is-the-safe-insert-function-of-the-manual-micromanipulator-and-how-does-it-work-478.html', 'https://www.presens.de/support-services/faqs/question/the-intensities-i-get-with-the-sensor-plates-are-very-low-for-my-reader-how-can-i-enhance-them-251.html', 'https://www.presens.de/support-services/faqs/question/what-is-the-difference-between-the-2-black-masks-for-the-sdr-the-sdr-osm24-and-sdr-msv24-1130.html', 'https://www.presens.de/support-services/faqs/question/is-one-biomass-calibration-function-valid-for-different-sfr-vario-devices-running-with-the-same-biol.html', 'https://www.presens.de/support-services/faqs/question/how-many-sensors-can-i-connect-to-a-microx-4-trace-oxygen-meter-is-it-a-4-channel-device-421.html', 'https://www.presens.de/support-services/faqs/question/how-can-i-rename-a-measurement-recorded-with-the-sdr-555.html', 'https://www.presens.de/support-services/faqs/question/how-long-can-i-use-a-sensordishr-231.html', 'https://www.presens.de/support-services/faqs/question/how-does-an-oxygen-sensor-work-3.html', 'https://www.presens.de/knowledge/basics/detail/oxygen-permeation-measurement-in-pet-bottles-1138.html', 'https://www.presens.de/support-services/faqs/question/what-types-of-temperature-sensors-are-used-with-the-presens-measurement-devices-433.html', 'https://www.presens.de/support-services/faqs/question/do-sensordishesr-come-sterile-61.html', 'https://www.presens.de/support-services/faqs/question/how-often-do-i-have-to-calibrate-the-sensor-plates-with-my-reader-253.html', 'https://www.presens.de/support-services/faqs/question/which-flasks-can-be-used-with-the-sfr-vario-486.html', 'https://www.presens.de/support-services/faqs/question/is-the-signal-transmitted-by-the-oxypror-an-electro-chemical-signal-1134.html', 'https://www.presens.de/support-services/faqs/question/how-long-can-i-measure-with-the-sfr-vario-battery-488.html', 'https://www.presens.de/knowledge/basics/detail/measurement-principle-of-the-visisenstm-imaging-systems-frim-902.html', 'https://www.presens.de/knowledge/basics/detail/microprofiling-1103.html', 'https://www.presens.de/support-services/faqs/question/does-the-ph-of-the-sample-affect-my-co2-sensor-reading-59.html', 'https://www.presens.de/support-services/faqs/question/how-long-do-i-need-to-equilibrate-before-starting-a-sdr-measurement-537.html', 'https://www.presens.de/support-services/faqs/question/the-needle-tip-of-the-microsensor-is-vibrating-or-not-moving-smoothly-when-i-try-to-insert-it-in-the.html', 'https://www.presens.de/support-services/faqs/question/is-the-sensor-spot-inside-the-sensorvials-for-read-out-with-the-sdr-the-same-as-the-ones-read-out-wi.html', 'https://www.presens.de/support-services/faqs/question/to-what-water-depth-can-i-use-the-oxy-flux-1210.html', 'https://www.presens.de/support-services/faqs/question/can-i-measure-inside-a-tissue-with-fiber-optic-microsensors-17.html', 'https://www.presens.de/knowledge/basics/detail/cultivation-of-bacteria-and-mammalian-cells-in-shake-flasks-1186.html', 'https://www.presens.de/support-services/faqs/question/is-there-a-standard-recommended-distance-to-place-the-polymer-optical-fiber-pof-from-the-sensor-sp.html', 'https://www.presens.de/support-services/faqs/question/the-stern-volmer-equation-33.html', 'https://www.presens.de/support-services/faqs/question/are-there-some-general-recommendations-for-measurements-with-the-sdr-557.html', 'https://www.presens.de/support-services/faqs/question/i-can-see-that-about-1-mm-of-the-tapered-sensor-tip-of-an-oxygen-microsensor-is-coated-with-material.html', 'https://www.presens.de/support-services/faqs/question/in-which-vessels-can-i-integrate-self-adhesive-ph-sensor-spots-sp-hp5-sa-or-sp-lg1-sa-1106.html', 'https://www.presens.de/support-services/faqs/question/when-do-i-adjust-humid-or-dry-measurement-settings-for-fibox-4-trace-microx-4-trace-ox.html', 'https://www.presens.de/support-services/faqs/question/can-i-change-the-cannula-on-my-profiling-microsensor-991.html', 'https://www.presens.de/knowledge/basics/detail/measurement-principle-of-chemical-optical-sensors-901.html', 'https://www.presens.de/support-services/faqs/question/how-do-i-use-the-oxygen-microsensor-for-measurement-in-ice-95.html', 'https://www.presens.de/support-services/faqs/question/is-the-temperature-which-i-see-in-the-maintenance-window-of-the-sdr-software-used-for-temperature-co.html', 'https://www.presens.de/support-services/faqs/question/i-use-a-glass-vessel-with-an-integrated-autoclavable-oxygen-sensor-how-do-i-remove-this-sensor-39.html', 'https://www.presens.de/support-services/faqs/question/what-is-the-difference-between-oxy-1-sma-and-oxy-1-st-1132.html', 'https://www.presens.de/support-services/faqs/question/is-there-a-recoating-service-for-the-needle-type-microsensors-476.html', 'https://www.presens.de/support-services/faqs/question/which-side-of-the-oxygen-sensor-spot-should-face-the-medium-9.html', 'https://www.presens.de/support-services/faqs/question/how-does-temperature-affect-my-ph-measurement-496.html', 'https://www.presens.de/support-services/faqs/question/how-can-i-clean-non-invasive-ph-sensors-43.html', 'https://www.presens.de/support-services/faqs/question/how-flexible-is-a-2-mm-polymer-optical-fiber-261.html', 'https://www.presens.de/support-services/faqs/question/can-i-measure-co2-also-in-a-gas-phase-or-only-in-liquid-phase-53.html', 'https://www.presens.de/support-services/faqs/question/how-does-salinity-affect-the-oxygen-measurement-103.html', 'https://www.presens.de/support-services/faqs/question/are-there-adapters-available-for-1-mm-fibers-used-with-microx-4-trace-or-oxy-1-st-trace-417.html', 'https://www.presens.de/support-services/faqs/question/can-i-use-ethanol-for-disinfecting-non-invasive-ph-sensors-45.html', 'https://www.presens.de/support-services/faqs/question/what-air-pressure-value-should-i-enter-in-the-sdr-software-where-do-i-get-it-from-543.html', 'https://www.presens.de/support-services/faqs/question/what-is-the-time-of-delivery-29.html', 'https://www.presens.de/support-services/faqs/question/i-forgot-to-change-the-oxygen-unit-in-the-sdr-software-from-the-default-unit-air-saturation-to-my.html', 'https://www.presens.de/support-services/faqs/question/can-i-use-the-sdr-for-hypoxic-measurements-565.html', 'https://www.presens.de/support-services/faqs/question/how-do-i-fix-the-sdr-on-a-shaker-227.html', 'https://www.presens.de/support-services/faqs/question/which-lengths-of-the-pofs-polymer-optical-fiber-are-available-31.html', 'https://www.presens.de/support-services/faqs/question/what-connection-type-does-the-oxy-flux-use-1209.html', 'https://www.presens.de/support-services/faqs/question/how-do-i-connect-my-oxypror-to-the-controller-1133.html', 'https://www.presens.de/support-services/faqs/question/how-do-i-measure-the-oxygen-content-in-small-headspace-packages-with-a-needle-type-oxygen-microsenso.html', 'https://www.presens.de/support-services/faqs/question/i-am-unable-to-connect-my-fibox-3-via-usb-to-my-windows-8-laptop-what-can-i-do-470.html', 'https://www.presens.de/support-services/faqs/question/how-do-i-calibrate-my-oxy-flux-eco-pst7-microsensor-1211.html', 'https://www.presens.de/support-services/faqs/question/i-use-the-oxohydrodish-ohd6-with-the-sdr-how-do-i-see-the-values-of-both-parameters-oxygen-and-p.html', 'https://www.presens.de/support-services/faqs/question/can-i-re-use-the-sensorvials-237.html', 'https://www.presens.de/support-services/faqs/question/does-the-sfr-sfr-vario-fit-into-my-incubator-shaker-81.html', 'https://www.presens.de/support-services/faqs/question/what-additional-features-does-the-presens-measurement-studio-2-have-which-applications-do-require-t.html', 'https://www.presens.de/support-services/faqs/question/can-i-use-the-same-meter-with-microsensors-non-invasive-sensors-and-invasive-probes-2.html', 'https://www.presens.de/support-services/faqs/question/which-side-of-the-ph-sensor-spot-should-face-the-medium-6.html', 'https://www.presens.de/support-services/faqs/question/the-filters-of-my-reader-do-not-exactly-match-the-combination-in-the-sensor-plates-technical-data.html', 'https://www.presens.de/support-services/faqs/question/what-is-the-difference-between-tapered-and-flat-broken-microsensor-tips-87.html', 'https://www.presens.de/support-services/faqs/question/which-types-and-sizes-of-shake-flasks-with-integrated-sensors-sfs-are-offered-by-presens-75.html', 'https://www.presens.de/support-services/faqs/question/which-measurement-interval-should-i-use-for-measurements-with-the-sdr-233.html', 'https://www.presens.de/support-services/faqs/question/can-i-sterilize-fiber-optic-sensors-25.html', 'https://www.presens.de/support-services/faqs/question/compensation-of-pressure-salinity-27.html', 'https://www.presens.de/support-services/faqs/question/how-is-the-sfr-sfr-vario-system-attached-to-the-shaker-492.html', 'https://www.presens.de/support-services/faqs/question/what-happens-if-the-temperature-changes-while-measuring-co2-55.html', 'https://www.presens.de/support-services/faqs/question/how-do-i-know-that-my-reader-gives-precise-results-with-the-sensor-plates-517.html', 'https://www.presens.de/support-services/faqs/question/what-happens-if-i-cross-the-30-c-line-during-measurement-with-the-sdr-549.html', 'https://www.presens.de/company/press/article/biomasse-in-schuettelkolbenkultur-886.html', 'https://www.presens.de/company/press/section/2.html', 'https://www.presens.de/company/press/article/real-life-cho-cultivation-in-single-use-bags-890.html', 'https://www.presens.de/company/press/section/3.html', 'https://www.presens.de/company/press/article/atp-synthese-ueber-oxidative-phosphorylierung-889.html', 'https://www.presens.de/company/press/article/shake-flask-feedback-controlled-feeding-891.html', 'https://www.presens.de/company/press/section/4.html', 'https://www.presens.de/company/press/article/die-haut-der-anderen-retten-887.html', 'https://www.presens.de/company/press/article/microfluidic-devices-888.html', 'https://www.presens.de/company/news/artikel/for-20-years-precision-sensing-around-the-world-107.html', 'https://www.presens.de/company/news/artikel/discover-the-new-presens-webpage-109.html', 'https://www.presens.de/company/news/page/2.html', 'https://www.presens.de/company/news/artikel/what-is-the-basic-measurement-principle-behind-presens-technology-134.html', 'https://www.presens.de/company/news/page/3.html', 'https://www.presens.de/company/news/page/11.html', 'https://www.presens.de/company/press/article/ready-to-use-devices-for-optimizing-bioprocesses-with-integrated-sensors-1009.html', 'https://www.presens.de/company/press/article/cytotoxicity-determination-1001.html', 'https://www.presens.de/company/press/article/noninvasive-oxygen-and-ph-sensors-1007.html', 'https://www.presens.de/company/press/article/non-invasive-method-for-monitoring-real-time-oxygen-concentrations-during-hspc-culture-1002.html', 'https://www.presens.de/company/press/article/single-use-containers-demand-single-use-sensors-1011.html', 'https://www.presens.de/company/press/article/non-invasive-optical-dissolved-oxygen-quantification-in-small-scale-bioreactors-1005.html', 'https://www.presens.de/company/press/article/quality-assessment-in-3d-cultures-of-disc-chondrocytes-1010.html', 'https://www.presens.de/company/press/article/process-monitoring-in-suspension-adapted-cho-cell-cultures-1012.html', 'https://www.presens.de/company/press/article/oxygen-in-action-1003.html', 'https://www.presens.de/company/press/article/novel-single-use-sensors-for-online-measurement-of-glucose-999.html', 'https://www.presens.de/company/press/article/enhancing-data-quality-with-a-partly-controllable-system-at-shake-flask-scale-998.html', 'https://www.presens.de/company/press/article/where-does-the-oxygen-go-1000.html', 'https://www.presens.de/company/press/article/co2-measurement-in-microfluidic-devices-892.html', 'https://www.presens.de/company/press/article/noninvasive-optical-sensor-technology-in-shake-flasks-for-mammalian-cell-cultures-1004.html', 'https://www.presens.de/company/press/article/growth-control-1008.html', 'https://www.presens.de/company/press/article/development-of-a-shaken-scale-down-model-1006.html', 'https://www.presens.de/company/news/artikel/do-you-need-exact-localized-point-measurements-126.html', 'https://www.presens.de/company/news/artikel/new-generation-of-shake-flasks-clamps-113.html', 'https://www.presens.de/company/news/artikel/vary-pressure-and-salinity-during-measurements-122.html', 'https://www.presens.de/company/news/artikel/optimize-cultivation-parameters-systematically-124.html', 'https://www.presens.de/company/news/artikel/caliplates-ease-ph-sensor-foil-calibration-111.html', 'https://www.presens.de/company/news/artikel/new-self-adhesive-technology-eases-ph-spot-integration-87.html', 'https://www.presens.de/company/news/artikel/strategic-alliance-for-better-bioproduct-quality-82.html', 'https://www.presens.de/company/news/artikel/get-a-glance-into-the-future-of-lab-technology-79.html', 'https://www.presens.de/company/news/artikel/image-low-ph-values-77.html', 'https://www.presens.de/company/news/artikel/analyze-your-shake-flask-culture-69.html', 'https://www.presens.de/company/news/artikel/presens-at-the-rewag-company-run-2015-71.html', 'https://www.presens.de/company/news/page/4.html', 'https://www.presens.de/company/news/artikel/larger-range-of-ready-to-use-sensor-flasks-available-now-84.html', 'https://www.presens.de/company/news/page/9.html', 'https://www.presens.de/company/news/page/10.html', 'https://www.presens.de/company/news/artikel/presens-precision-sensing-gmbh-eleven-years-of-unbroken-success-5.html', 'https://www.presens.de/company/news/artikel/presens-team-participates-in-2014-regensburg-company-run-63.html', 'https://www.presens.de/company/news/artikel/half-way-around-the-globe-for-science-105.html', 'https://www.presens.de/company/news/artikel/make-metabolic-shifts-visible-73.html', 'https://www.presens.de/company/news/page/5.html', 'https://www.presens.de/company/news/artikel/high-flexibility-for-monitoring-perfusion-systems-75.html', 'https://www.presens.de/company/news/artikel/a-look-behind-the-scenes-at-presens-65.html', 'https://www.presens.de/company/news/artikel/keep-control-over-your-microsensor-measurements-66.html', 'https://www.presens.de/company/news/artikel/presens-supports-efforts-to-strengthen-white-biotechnology-17.html', 'https://www.presens.de/company/news/artikel/patients-will-benefit-from-fast-sensor-response-25.html', 'https://www.presens.de/company/news/artikel/presens-website-now-shows-add-on-products-15.html', 'https://www.presens.de/company/news/artikel/answers-to-your-questions-19.html', 'https://www.presens.de/company/news/artikel/the-future-of-single-use-manufacturing-systems-23.html', 'https://www.presens.de/company/news/artikel/quality-first-and-foremost-21.html', 'https://www.presens.de/company/news/page/8.html', 'https://www.presens.de/company/news/artikel/presens-now-en-iso-certified-7.html', 'https://www.presens.de/company/news/artikel/presens-now-member-of-bpsa-9.html', 'https://www.presens.de/company/news/artikel/presens-precision-sensing-gmbh-launches-sfr-3.html', 'https://www.presens.de/company/news/artikel/new-website-launched-1.html', 'https://www.presens.de/company/news/artikel/line-of-multiwell-plates-formats-for-sdr-extended-11.html', 'https://www.presens.de/company/news/artikel/presens-supports-duranr-13.html', 'https://www.presens.de/company/news/page/6.html', 'https://www.presens.de/company/news/artikel/catchy-booth-for-product-launch-102.html', 'https://www.presens.de/company/news/artikel/a-new-generation-of-oxygen-meters-fibox-4-fibox-4-trace-61.html', 'https://www.presens.de/company/news/artikel/pick-the-parameters-of-interest-101.html', 'https://www.presens.de/company/news/artikel/our-winners-of-this-years-visisens-competition-104.html', 'https://www.presens.de/company/news/artikel/taking-tissue-engineering-to-the-next-level-103.html', 'https://www.presens.de/company/news/artikel/advanced-technology-for-cell-therapy-products-99.html', 'https://www.presens.de/services/faqs.html', 'https://www.presens.de/company/news/artikel/seeing-the-invisible-now-possible-31.html', 'https://www.presens.de/company/news/page/7.html', 'https://www.presens.de/company/news/artikel/vital-parameters-kept-under-surveillance-29.html', 'https://www.presens.de/company/news/artikel/research-on-hypoxia-using-presens-oxygen-microsensors-raises-great-interest-37.html', 'https://www.presens.de/company/news/artikel/what-your-cells-see-47.html', 'https://www.presens.de/company/news/artikel/fast-sensor-response-increases-the-chances-for-patients-33.html', 'https://www.presens.de/company/news/artikel/dr-shaker-offers-sound-advice-27.html', 'https://www.presens.de/company/news/artikel/and-the-winners-are-93.html', 'https://www.presens.de/company/news/artikel/the-smallest-devices-ensure-highest-productivity-83.html', 'https://www.presens.de/company/news/artikel/maximising-the-efficiency-of-tomorrows-bioprocess-production-94.html', 'https://www.presens.de/company/news/artikel/on-the-right-track-to-nitrogen-monoxide-monitoring-90.html', 'https://www.presens.de/company/news/artikel/industry-insiders-elect-visisens-as-one-of-the-top-innovations-2012-91.html', 'https://www.presens.de/company/news/artikel/understanding-the-impact-of-ocean-acidification-92.html', 'https://www.presens.de/industries/scientific-r-d.html', 'https://www.presens.de/company/news/artikel/plants-under-stress-preparing-cereal-crops-for-climate-change-81.html', 'https://www.presens.de/company/news/artikel/sensor-engineering-saves-both-time-and-money-53.html', 'https://www.presens.de/company/news/artikel/parallel-bioprocess-development-tool-on-cell-culture-tubes-49.html', 'https://www.presens.de/company/news/artikel/scientists-talking-the-same-language-55.html', 'https://www.presens.de/company/news/artikel/seeing-metabolic-activity-45.html', 'https://www.presens.de/company/news/artikel/conquer-ultra-barrier-properties-51.html', 'http://www.datamining-international.com/?page_id=11258', 'http://www.datamining-international.com/?page_id=11352', 'http://www.datamining-international.com/?page_id=11287', 'http://www.datamining-international.com/?page_id=11377', 'http://www.datamining-international.com/?page_id=11261', 'http://www.datamining-international.com/?page_id=11248', 'http://www.datamining-international.com/?page_id=11319', 'http://www.datamining-international.com/?page_id=11385', 'http://www.datamining-international.com/?page_id=11328', 'http://www.datamining-international.com/?page_id=11301', 'http://www.datamining-international.com/?page_id=11195', 'http://www.datamining-international.com/?page_id=11458', 'http://www.datamining-international.com/?p=12442', 'http://www.datamining-international.com/?author=1', 'http://www.datamining-international.com/?page_id=11220', 'http://www.datamining-international.com/?page_id=11360', 'http://www.datamining-international.com/?p=12439', 'http://www.datamining-international.com/?page_id=11199', 'http://www.datamining-international.com/?p=12446', 'http://www.datamining-international.com/?p=12456', 'http://www.datamining-international.com/new/?page_id=11360', 'http://www.datamining-international.com/new/?page_id=11151', 'http://www.datamining-international.com/new/?page_id=11377', 'http://www.datamining-international.com/new/?page_id=11199', 'http://www.datamining-international.com/new/?page_id=11580', 'http://www.datamining-international.com/new/?page_id=11583', 'http://www.datamining-international.com/?p=12366', 'http://www.datamining-international.com/?p=12381', 'http://www.datamining-international.com/?p=12337', 'http://www.datamining-international.com/?p=12342', 'http://www.datamining-international.com/?p=12312', 'http://www.datamining-international.com/?p=12385', 'http://www.datamining-international.com/?attachment_id=12396', 'http://www.datamining-international.com/?page_id=11580', 'http://www.datamining-international.com/?page_id=11136', 'http://www.datamining-international.com/?page_id=11139', 'http://www.datamining-international.com/?page_id=11583', 'http://www.datamining-international.com/?page_id=11142', 'http://www.datamining-international.com/?cat=42', 'http://www.datamining-international.com/?p=12278', 'http://www.datamining-international.com/?p=12261', 'http://www.datamining-international.com/?p=12038', 'http://www.datamining-international.com/?p=11708', 'http://www.datamining-international.com/?p=12192', 'http://www.datamining-international.com/?p=12201', 'http://www.entelechon.com/en/next-generation-sequencing/rfi/', 'http://www.entelechon.com/en/dna-rna-oligonucleotides/custom-dna-oligos/extremers/', 'http://www.entelechon.com/en/dna-rna-oligonucleotides/custom-rna-oligos/ivt-rna/', 'http://www.entelechon.com/en/ecom/oligonucleotides/optimised-application-oligos/synbio-oligo/', 'http://www.entelechon.com/en/eurofins-genomics/product-faqs/next-generation-sequencing/questions-on-bioinformatic-services/what-does-clustering-mean/', 'http://www.entelechon.com/en/eurofins-genomics/product-faqs/next-generation-sequencing/transcriptome-profiling-favourite/replacement-samples/', 'http://www.entelechon.com/en/ecom/oligonucleotides/oligo-projects/', 'http://www.entelechon.com/en/ecom/oligonucleotides/optimised-application-oligos/cloning-oligos-plates/', 'http://www.entelechon.com/en/ecom/oligonucleotides/', 'http://www.entelechon.com/en/ecom/oligonucleotides/optimised-application-oligos/pcr-primer-plates/', 'http://www.entelechon.com/en/custom-dna-sequencing/additional-services/sample-submission/', 'http://www.entelechon.com/en/next-generation-sequencing/sample-submission-information-for-individual-projects/', 'http://www.entelechon.com/en/next-generation-sequencing/rfi.aspx', 'http://www.axoscience.com/rd-projects/fui-hifi-cap-2/', 'http://www.axoscience.com/rd-projects/fui-hifi-cap/', 'http://www.sintesiresearch.com/medical-writing-clinical-services.html', 'http://www.sintesiresearch.com/drug-surveillance-clinical-services.html', 'http://www.sintesiresearch.com/drug-management-clinical-services.html', 'http://www.particlesciences.com/news/technical-briefs/', 'http://www.particlesciences.com/services/drug-release-testing/', 'http://www.particlesciences.com/services/drug-device-combination-products/', 'http://www.particlesciences.com/news/technical-briefs/2012/process-analytical-technology.html', 'http://www.aqix.com/metabolites.php', 'http://www.biopharmachemireland.ie/IBEC/IBEC.nsf/vPages/Events~Ibec_Regional_Insights_Series_2017~cork!OpenDocument', 'https://www.gedeonprogrammes.com/en/gedeon-programmes/gedeon-programmes-2/', 'http://www.medical-prognosis.com/investor-and-media/20170322-interview-with-mpi-ov-in/', 'http://www.medical-prognosis.com/investor-and-media/20161230-mpi-and-ov-enters-exclusivity-and-ownership-agreements-of-spvs-financing-secured-for-the-first-two-spvs/', 'http://www.medical-prognosis.com/investor-and-media/20160512-mpi-positive-data-on-mpis-drp-for-5fu-published-in-plos-one/', 'http://www.medical-prognosis.com/investor-and-media/20160219-mpi-raises-dkk-8686575-in-private-placement-at-a-price-of-135/', 'http://www.medical-prognosis.com/investor-and-media/20170831-mpi-mpi-publishes-halfyear-report-for-the-first-half-of-2017/', 'http://www.medical-prognosis.com/investor-and-media/20140812-medical-prognosis-institute-as-interim-report-first-half-2014/', 'http://www.medical-prognosis.com/investor-and-media/20160602-meet-mpi-at-sachs-immunooncology-bd-asco-american-society-of-clinical-oncology-chicago-bio-in-san-francisco/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20180322-mpi-scientific-journal-highlights-study-of-the-drp-tool-in-cisplatin-treatment-for-patients-with-lung-cancer/', 'http://www.medical-prognosis.com/investor-and-media/20170519-medical-prognosis-institute-as-presents-at-prohearings-in-stockholm/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20170124-drp-successfully-predicts-effect-of-4-breast-cancer-drugs-for-personalized-medicine/', 'http://www.medical-prognosis.com/investor-and-media/20161103-mpi-increases-its-capital-with-nominal-dkk-2000-as-a-result-of-exercise-of-40000-warrants/', 'http://www.medical-prognosis.com/investor-and-media/20150605-oncology-venture-sweden-ab-a-spinout-from-mpi-announces-its-ipo-at-the-swedish-aktietorget/', 'http://www.medical-prognosis.com/investor-and-media/20150326-medical-prognosis-institute-as-publishes-annual-report-2014/', 'http://www.medical-prognosis.com/investor-and-media/20140403-mpi-and-td2-join-in-strategic-collaboration-to-provide-drug-developers-a-unique-multi-biomarker-direct-path-to-drug-approval/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20170519-mpi-medwatch-article-about-mpi/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20160914-mpis-prp-for-precision-medicine-to-be-studied-with-breast-cancer-experts/', 'http://www.medical-prognosis.com/investor-and-media/20180327-claus-frisenberg-pedersen-cfo-in-oncology-venture-buys-shares-in-oncology-venture-and-mpi/', 'http://www.medical-prognosis.com/investor-and-media/20140527-mpi-and-liplasome-present-the-phase-1-study-with-liplacis-at-the-asco-congress-monday-2-in-chicago-at-8am-local-time/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20140912-mpi-is-today-publishing-a-prospectus-in-connection-with-an-offering-of-a-minimum-of-44330-and-up-to-104064-new-shares-of-dkk-100-nominal-value-each-at-a-price-of-dkk-18000-per-new-share/', 'http://www.medical-prognosis.com/investor-and-media/20160218-mpi-issues-warrants/', 'http://www.medical-prognosis.com/investor-and-media/20151127-mpi-unblinds-prospective-study-of-lungchip-prognosticator-in-early-lung-cancer/', 'http://www.medical-prognosis.com/investor-and-media/20150827-mpi-will-publish-its-halfyear-report-for-the-first-half-year-of-2015-on-august-31st/', 'http://www.medical-prognosis.com/investor-and-media/20160614-mpi-update-on-warrant-program/', 'http://www.medical-prognosis.com/investor-and-media/20170328-mpis-spinout-oncology-venture-inlicenses-2bbbs-phase-2-lead-product-2b3101-for-2x-oncologys-pipeline/', 'http://www.medical-prognosis.com/investor-and-media/20170711-mpi-last-day-of-trading-in-paid-subscription-shares/', 'http://www.medical-prognosis.com/investor-and-media/20160920-mpis-spinout-oncology-venture-signs-partnership-deal-with-cadila-pharmaceuticals-on-liplacis-using-mpis-drp-technology/', 'http://www.medical-prognosis.com/investor-and-media/20140409-notice-of-annual-general-meeting-in-medical-prognosis-institute-as/', 'http://www.medical-prognosis.com/investor-and-media/20180131-mpis-spinout-oncology-venture-announces-positive-interim-results-from-a-phase-12-drp-guided-study-of-liplacis-in-heavily-pretreated-breast-cancer-patients/', 'http://www.medical-prognosis.com/investor-and-media/20170308-exercise-of-warrants-in-oncology-venture-sweden-ab/', 'http://www.medical-prognosis.com/investor-and-media/20170421-mpi-increases-its-share-capital-with-nominal-dkk-6190-as-a-result-of-exercise-of-123800-warrants/', 'http://www.medical-prognosis.com/investor-and-media/20170331-mpi-publishes-annual-report-for-2016/', 'http://www.medical-prognosis.com/investor-and-media/20160316-mpi-increases-its-capital-by-2000-shares-as-a-result-of-warrant-exercise/', 'http://www.medical-prognosis.com/investor-and-media/20150831-medical-prognosis-institute-as-interim-report-first-half-2015/', 'http://www.medical-prognosis.com/investor-and-media/20170609-mpi-2x-oncology-inc-presents-at-jefferies-global-healthcare-conference-live-webcast/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20170324-mpis-spinout-oncology-venture-to-evaluate-eisai-oncology-drug-for-inlicense-to-2x-oncology-inc/', 'http://www.medical-prognosis.com/investor-and-media/20140910-mpi-pr%c3%a6senterer-data-pa-esmo/?origin=event', 'http://www.medical-prognosis.com/investor-and-media/20150904-mpi-announces-3-abstracts-on-the-aacrncieortc-international-conference-on-molecular-targets-and-cancer-therapeutics-in-boston/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20160318-mpi-medical-prognosis-institute-as-publishes-annual-report-2015/', 'http://www.medical-prognosis.com/investor-and-media/20151107-new-academic-drug-screening-platform-for-cancer-treatment/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20160831-mpi-interim-report-first-half-2016/', 'http://www.medical-prognosis.com/investor-and-media/20160405-interview-with-ceo-peter-buhl-jensen-available/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20150428-oncology-venture-mpis-drug-development-arm-raises-more-than-6-million-dkk-from-private-investors/', 'http://www.medical-prognosis.com/investor-and-media/20160209-mpi-summary-of-extraordinary-general-meeting/', 'http://www.medical-prognosis.com/investor-and-media/20160406-indkaldelse-til-ordin%c3%a6r-generalforsamling/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20150602-foredrag-pa-aktion%c3%a6rmessen-i-arhus/?origin=event', 'http://www.medical-prognosis.com/investor-and-media/20170823-mpi-drp-to-be-evaluated-in-6-to-7-prospective-studies/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20160927-mpi-granted-patent-on-the-drug-response-predictor-technology-in-china/', 'http://www.medical-prognosis.com/investor-and-media/20160527-fly-fishing-and-treating-cancer-same-same-but-different-thomas-jensen-tedx-bozeman/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20170919-mpi-liplacis-phase-2-recruitment-ongoing-in-drp-screened-breast-cancer-patients-relevant-clinical-benefits-in-3-out-of-5-treated-patients/', 'http://www.medical-prognosis.com/investor-and-media/20160128-mpi-is-issued-patent-in-australia/', 'http://www.medical-prognosis.com/investor-and-media/20170224-mpi-communique-from-the-egm-of-mpi-24-february-2017/', 'http://www.medical-prognosis.com/investor-and-media/20180313-medical-prognosis-institute-publishes-selected-financial-information-for-the-period-1-july-2017-31-december-2017-due-to-the-proposed-merger-between-medical-prognosis-institute-and-oncology-venture/', 'http://www.medical-prognosis.com/investor-and-media/20170322-interview-with-mpi-ov-in/?origin=event', 'http://www.medical-prognosis.com/investor-and-media/20160413-peter-buhl-jensen-talks-about-the-digital-transformation-in-pharma/?origin=event', 'http://www.medical-prognosis.com/investor-and-media/20170322-interview-with-medical-prognosis-institute-and-oncology-venture-in-million%c3%a6rklubben/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20160219-mpis-spinout-ov-has-inlicensed-liplacistm/', 'http://www.medical-prognosis.com/investor-and-media/20131023-mpi-receives-35-million-dkk-from-the-danish-market-development-fund-to-develop-the-genetest-lung-prognosticator/', 'http://www.medical-prognosis.com/investor-and-media/20160823-first-drp-selected-breast-cancer-patient-obtained-reduction-of-tumor-by-liplacis-treatment/', 'http://www.medical-prognosis.com/investor-and-media/20160128-correction-mpi-is-issued-patent-in-australia/', 'http://www.medical-prognosis.com/investor-and-media/20171214-result-of-evaluation-of-drp-for-tki-drug-from-big-pharma-available-third-week-of-january-2018/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20170823-mpi-2x-oncologys-ceo-george-o-elstons-newsletter-to-shareholders/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20180309-proposed-merger-between-medical-prognosis-institute-and-oncology-venture/', 'http://www.medical-prognosis.com/investor-and-media/20170804-mpi-artikel-om-mpi-og-oncology-venture-i-medwatch/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20170707-mpi-oncology-venture-and-eisai-forge-exclusive-global-license-agreement-for-clinical-stage-oncology-drug-parp-inhibitor-e7449-2x121/', 'http://www.medical-prognosis.com/investor-and-media/20170809-mpi-investor-analysis-of-oncology-venture-sweden-ab/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20180323-mpi-publishes-annual-report-for-2017/', 'http://www.medical-prognosis.com/investor-and-media/20171215-drug-response-prediction-in-highrisk-multiple-myeloma-prediction-of-melphalan-and-bortezomib-response/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20171101-mpi-announces-registration-of-trademark-for-drp/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20160315-mpi-will-publish-its-annual-report-2015-on-march-18th/', 'http://www.medical-prognosis.com/investor-and-media/20170119-mpis-spinout-oncology-venture-granted-eurostars-funding-for-poc-of-liplacis/', 'http://www.medical-prognosis.com/investor-and-media/20160420-medical-prognosis-institute-as-forl%c3%b8b-af-ordin%c3%a6r-generalforsamling/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20160409-mpi-see-mpis-cto-thomas-jensen-at-tedx-bozeman-on-april-9th/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20160705-mpi-and-oncology-venture-enhances-the-collaboration-by-entering-another-agreement-on-drps/', 'http://www.medical-prognosis.com/investor-and-media/20160304-mpis-spinout-oncology-venture-to-present-liplacis-doseescalating-poc-study-at-the-aacr-annual-meeting-2016-in-new-orleans/', 'http://www.medical-prognosis.com/investor-and-media/20170602-meet-medical-prognosis-institute-at-american-society-of-clinical-oncology-asco-chicago/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20160316-sedermeradagen-lund-2016/?origin=event', 'http://www.medical-prognosis.com/investor-and-media/20170518-the-efficacy-of-chemotherapy-with-epirubicin-one-the-of-most-used-drugs-in-breast-cancer-can-now-be-predicted-by-drp-data-published-at-asco/', 'http://www.medical-prognosis.com/investor-and-media/20140523-mpi-increases-its-capital-by-67774-shares-as-a-result-of-the-capital-increase-adopted-on-the-annual-general-meeting-held-on-24-april-2014/', 'http://www.medical-prognosis.com/investor-and-media/20150629-mpis-spinout-oncology-venture-announces-oversubscription-of-370-of-its-emission-prior-to-listing-at-the-aktietorget/', 'http://www.medical-prognosis.com/investor-and-media/20170222-mpi-communique-from-the-extraordinary-shareholders-meeting-of-mpi/', 'http://www.medical-prognosis.com/investor-and-media/20160928-abstracts-for-european-society-of-medical-oncology-esmo-available-online-on-wednesday-28th-september-2016-1200-cet/', 'http://www.medical-prognosis.com/investor-and-media/20160609-mpi-update-on-date-of-first-day-of-trading-on-nasdaq-first-north-stockholm/', 'http://www.medical-prognosis.com/investor-and-media/20170614-medical-prognosis-institute-as-announces-start-of-subscription-period-for-rights-issue/', 'http://www.medical-prognosis.com/investor-and-media/20170425-communique-annual-general-meeting-april-2017/', 'http://www.medical-prognosis.com/investor-and-media/20160217-mpi-publishes-positive-results-with-drptm-tool-in-gastroesophageal-cancer/', 'http://www.medical-prognosis.com/investor-and-media/20141105-mpi-and-alion-pharmaceuticals-inc-establish-partnership-to-develop-drug-response-predictors-for-ion-channel-inhibitors-in-oncology/', 'http://www.medical-prognosis.com/investor-and-media/20170109-mpis-drp-for-oncology-ventures-lead-product-liplacis-registered-for-cemarking-in-eu/', 'http://www.medical-prognosis.com/investor-and-media/20170105-mpi-increases-its-share-capital-with-nominal-dkk-6337-as-a-result-of-exercise-of-126740-warrants/', 'http://www.medical-prognosis.com/investor-and-media/20170529-successful-us-patent-strategy-oncology-ventures-irofulven-claims-accepted/', 'http://www.medical-prognosis.com/investor-and-media/20131104-mpi-presents-data-on-its-drug-response-predictor-technology-that-can-predict-which-indication-will-be-approved-by-the-fda-on-the-adapt-congress-in-boston/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20170531-mpis-spinout-oncology-ventures-second-drug-candidate-in-the-clinic-first-multiple-myeloma-patient-in-study-with-apo010-an-immunooncology-drug/', 'http://www.medical-prognosis.com/investor-and-media/20160310-first-patient-included-in-apo010-immunooncology-screening-trial-by-mpis-spinout-oncology-venture/', 'http://www.medical-prognosis.com/investor-and-media/20150529-mpis-drug-development-arm-oncology-venture-and-lantern-pharma-announce-partnership-to-advance-irofulven-for-metastatic-prostate-cancer/', 'http://www.medical-prognosis.com/investor-and-media/20150428-oncology-venture-mpis-drug-development-arm-raises-more-than-6-million-dkk-from-private-investors/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20170601-the-board-of-mpi-resolves-to-conduct-a-rights-issue-of-new-shares/', 'http://www.medical-prognosis.com/investor-and-media/20170608-mpi-ovs-spinout-2x-oncology-obtains-us-ind-for-2x111/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20170627-cancer-response-to-ovs-liplacis-successfully-predicted-in-early-data-by-mpis-drp-technology/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20140424-medical-prognosis-institute-as-passing-of-annual-general-meeting/', 'http://www.medical-prognosis.com/investor-and-media/20140815-mpi-notice-of-extraordinary-general-meeting-in-medical-prognosis-institute-as/', 'http://www.medical-prognosis.com/investor-and-media/20150304-oncology-venture-mpis-drug-development-arm-and-lantern-pharma-receive-icip-grant-to-advance-irofulven-for-metastatic-prostate-cancer/', 'http://www.medical-prognosis.com/investor-and-media/20160831-correction-mpi-interim-report-first-half-2016/', 'http://www.medical-prognosis.com/investor-and-media/20150601-medical-prognosis-institute-and-nemucore-announce-strategic-partnership/', 'http://www.medical-prognosis.com/investor-and-media/20160122-mpi-notice-of-extraordinary-general-meeting/', 'http://www.medical-prognosis.com/investor-and-media/20170425-interview-with-oncology-venture-sweden-ab-in-berlingske-tidende/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20160621-mpi-is-listing-on-nasdaq-stockholm-first-north-first-day-of-trading-is-june-27th-2016/', 'http://www.medical-prognosis.com/investor-and-media/20140327-medical-prognosis-institute-as-annual-report-2013/', 'http://www.medical-prognosis.com/investor-and-media/20150505-oncology-venture-mpis-spin-off-company/?origin=event', 'http://www.medical-prognosis.com/investor-and-media/20170705-mpi-raised-sek-103-million-in-rights-issue/', 'http://www.medical-prognosis.com/investor-and-media/20170313-meet-medical-prognosis-institute-at-investordagen-in-copenhagen-march-21st-2017-get-your-free-ticket-here/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20170207-mpi-notice-to-convene-extraordinary-general-meeting-warrants/', 'http://www.medical-prognosis.com/investor-and-media/20160224-mpi-registration-of-capital-increase-completed/', 'http://www.medical-prognosis.com/investor-and-media/20170719-mpi-ov-to-evaluate-the-potential-of-inlicensing-a-small-molecule-compound-for-development-in-cancer-from-a-major-pharmaceutical-company/', 'http://www.medical-prognosis.com/investor-and-media/20151108-drptm-enables-irofulven-clinical-trial-in-prostate-cancer/', 'http://www.medical-prognosis.com/investor-and-media/20180115-mpis-spinout-oncology-venture-will-execute-license-to-multi-tki-phase-3-compound/', 'http://www.medical-prognosis.com/investor-and-media/20160427-mpi-and-oncology-venture-enters-three-new-agreements-on-drps/', 'http://www.medical-prognosis.com/investor-and-media/20151207-mpi-and-mundipharma-edo-gmbh-enters-agreement-of-drptm-for-their-anti-cancer-lead-compound-edos101-in-clinical-trials/', 'http://www.medical-prognosis.com/investor-and-media/20160503-mpi-process-started-regarding-change-of-marketplace/', 'http://www.medical-prognosis.com/investor-and-media/20140902-medical-prognosis-institute-as-passing-of-extraordinary-general-meeting/', 'http://www.medical-prognosis.com/investor-and-media/20150226-mpi-increases-its-capital-by-2000-shares-as-a-result-of-warrant-exercise/', 'http://www.medical-prognosis.com/investor-and-media/20160531-mpis-drp-used-in-the-first-prospective-study/', 'http://www.medical-prognosis.com/investor-and-media/20170207-mpi-notice-to-convene-extraordinary-general-meeting/', 'http://www.medical-prognosis.com/investor-and-media/20140425-mpi-increases-its-capital-by-21500-shares-as-a-result-of-employee-warrant-exercise/', 'http://www.medical-prognosis.com/investor-and-media/20151222-mpi-participates-at-biotech-showcase-in-san-francisco/?origin=announcements', 'http://www.medical-prognosis.com/investor-and-media/20160909-mpis-spinout-oncology-venture-incorporates-2x-oncology-inc-a-womens-cancer-company-in-the-us/', 'http://www.medical-prognosis.com/investor-and-media/20160526-mpi-presents-at-sedermeradagen-in-gothenburg/?origin=announcements', 'http://www.synkola.sk/bb.php', 'http://www.synkola.sk/leado.php', 'http://www.synkola.sk/leadf.php', 'http://www.neurix.ch/neurix-co-develops-technology-in-neurotransmitters', 'http://www.neurix.ch/neurix-in-a-european-consortium-focusing-on-neuroinflammation', 'http://www.biovectis.com/forensic1/mixed-dna-samples', 'http://www.biovectis.com/life-science-rd-tools/power-supplies', 'http://www.etherna.be/mrna-production', 'http://www.vaccibody.com/board-of-directors/', 'http://www.vaccibody.com/media/', 'http://www.elekta.com/company/awards/', 'http://www.elekta.com/radiotherapy/treatment-delivery-systems/', 'http://www.elekta.com/radiotherapy/treatment-solutions/', 'https://www.elekta.com/company/awards/', 'http://www.elekta.com/radiotherapy/treatment-solutions.html', 'http://www.elekta.com/radiotherapy/treatment-delivery-systems.html', 'http://www.elekta.com/company/awards.html', 'http://www.imp.ac.at', 'http://www.imp.ac.at/groups/tim-clausen/', 'http://www.imp.ac.at/#content', 'http://www.imp.ac.at/about/imp-at-a-glance/', 'http://www.becker-hickl.de/IFP-201_.htm', 'http://www.becker-hickl.de/bdl-smy.htm', 'http://www.becker-hickl.de/bds-mm.htm', 'http://www.becker-hickl.de/bdl-sm.htm', 'http://www.becker-hickl.de/id220.htm', 'https://www.acsbiomarker.com/rna-extraction', 'http://www.in2care.org/research/industrial-scale-production-of-eave-tube-inserts-for-malaria-control-in-africa-2015-2016/', 'http://www.in2care.org/research/projects/paint-against-dengue-mosquitoes/', 'http://www.igeamedical.com/clinical-evidence/oncology-resources/local-recurrences-and-skin-metastases-breast-cancer/treatment-e', 'http://www.igeamedical.com/clinical-evidence/oncology-resources/local-recurrences-and-skin-metastases-breast-cancer/treatment-0', 'http://www.igeamedical.com/clinical-evidence/oncology-resources/non-melanoma-skin-cancers/treatment-efficacy-electrochemotherap', 'http://www.igeamedical.com/clinical-evidence/oncology-resources/melanoma/treatment-efficacy-electrochemotherapy-multi-instituti', 'http://www.igeamedical.com/clinical-evidence/oncology-resources/melanoma/utility-electrochemotherapy-melanoma-treatment', 'http://www.igeamedical.com/clinical-evidence/oncology-resources/melanoma/treatment-metastatic-melanoma-electrochemotherapy', 'http://www.syreon.eu/news/essential-medicine-list-in-ukraine', 'http://www.syreon.eu/news/sri-is-now-a-recognized-research-entity-by-eurostat', 'http://www.bactiguard.com/en/news-and-press/press-releases/growing-interest-in-infection-prevention-in-the-middle-east', 'http://www.bactiguard.com/en/news-press/news/good-to-great-tennis-academy-newsletter-5', 'http://www.bactiguard.com/en/news-press/news/good-to-great-tennis-academy-newsletter-6', 'http://www.bactiguard.com/en/news-press/news/good-to-great-tennis-academy-newsletter-7', 'http://www.bactiguard.com/en/node/1370980', 'http://www.bactiguard.com/en/node/1370981', 'http://www.bactiguard.com/en/node/1371035', 'http://www.bactiguard.com/en/node/1371029', 'http://www.bactiguard.com/en/news-press/news/good-to-great-tennis-academy-newsletter-8', 'http://www.bactiguard.com/en/news-press/news/good-to-great-tennis-academy-newsletter-9', 'http://www.bactiguard.com/en/node/1370972', 'http://www.bactiguard.com/en/news-press/news/good-to-great-tennis-academy-newsletter-1', 'http://www.bactiguard.com/en/news-press/news/good-to-great-tennis-academy-newsletter', 'http://www.bactiguard.com/en/news-press/news/good-to-great-tennis-academy-newsletter-0', 'http://www.bactiguard.com/en/node/1370992', 'http://www.bactiguard.com/en/node/1370988', 'http://www.bactiguard.com/en/news-press/news/good-to-great-tennis-academy-newsletter-3', 'http://www.bactiguard.com/en/news-press/news/good-to-great-tennis-academy-newsletter-4', 'http://www.bactiguard.com/en/news-press/news/good-to-great-tennis-academy-newsletter-2', 'http://www.bactiguard.com/en/node/1371001', 'http://www.bactiguard.com/en/node/1371005', 'http://www.bactiguard.com/en/node/1371016', 'http://www.bactiguard.com/en/node/1371024', 'http://www.bactiguard.com/en/node/1371019', 'http://www.bactiguard.com/en/node/1371186', 'http://www.bactiguard.com/en/node/1371083', 'http://www.bactiguard.com/en/node/1371059', 'http://www.bactiguard.com/en/node/1371075', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/590/', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/590/pieris-pharmaceuticals-reports-full-year-2017-financial', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/583/pieris-pharmaceuticals-and-seattle-genetics-announce', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/589/pieris-pharmaceuticals-to-present-at-investor-conferences', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/582/pieris-pharmaceuticals-to-host-key-opinion-leader-event-on', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/588/pieris-pharmaceuticals-to-host-full-year-2017-investor-call', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/587/pieris-pharmaceuticals-to-present-at-the-rbc-capital', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/550/pieris-pharmaceuticals-and-servier-forge-strategic', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/575/pieris-pharmaceuticals-announces-dosing-of-first-patient-in', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/580/pieris-pharmaceuticals-appoints-james-geraghty-as-chairman', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/577/pieris-pharmaceuticals-to-present-at-investor-conferences', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/578/pieris-pharmaceuticals-to-host-third-quarter-2017-investor', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/574/pieris-pharmaceuticals-to-present-at-the-leerink-partners', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/571/pieris-pharmaceuticals-to-host-second-quarter-2017-investor', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/84/pieris-raises-25-m-us-38-m-in-series-b-financing', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/545/pieris-pharmaceuticals-to-receive-glp-tox-milestone-payment', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/546/pieris-pharmaceuticals-to-host-third-quarter-2016-investor', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/543/pieris-pharmaceuticals-presents-positive-data-for-its-lead', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/540/pieris-pharmaceuticals-to-present-at-rodman-renshaw-18th', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/516/pieris-pharmaceuticals-to-host-third-quarter-2015-investor', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/522/pieris-pharmaceuticals-achieves-payment-milestone-in-sanofi', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/523/pieris-pharmaceuticals-to-present-at-the-oppenheimer-26th', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/565/pieris-pharmaceuticals-appoints-james-geraghty-to-its-board', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/561/pieris-pharmaceuticals-to-host-first-quarter-2017-investor', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/566/pieris-pharmaceuticals-to-present-at-the-jefferies-2017', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/563/pieris-pharmaceuticals-to-host-conference-call-on-strategic', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/569/pieris-pharmaceuticals-added-to-the-russell-2000r-and', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/552/pieris-pharmaceuticals-to-present-at-the-bio-ceo-investor', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/559/pieris-pharmaceuticals-reports-full-year-2016-financial', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/558/pieris-pharmaceuticals-to-host-full-year-2016-investor-call', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/554/pieris-pharmaceuticals-to-present-at-the-cowen-and-company', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/557/pieris-pharmaceuticals-to-present-at-oppenheimers-27th', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/556/pieris-pharmaceuticals-to-present-at-the-29th-annual-roth', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/560/pieris-pharmaceuticals-presents-ind-enabling-data-for', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/549/pieris-pharmaceuticals-to-host-investor-call-today-to', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/538/pieris-pharmaceuticals-to-host-second-quarter-2016-investor', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/537/pieris-pharmaceuticals-appoints-julian-adams-ph-d-to-its', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/532/pieris-pharmaceuticals-to-host-first-quarter-2016-investor', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/531/pieris-pharmaceuticals-reports-full-year-2015-financial', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/527/pieris-pharmaceuticals-to-present-at-the-28th-annual-roth', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/526/pieris-pharmaceuticals-to-present-at-the-18th-annual-bio', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/528/pieris-pharmaceuticals-to-present-at-the-cowen-company', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/529/pieris-pharmaceuticals-to-host-full-year-2015-investor-call', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/510/pieris-pharmaceuticals-to-present-at-the-17th-annual-rodman', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/511/pieris-pharmaceuticals-collaborator-presents-promising', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/512/pieris-pharmaceuticals-presents-positive-preclinical-data', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/503/pieris-pharmaceuticals-closes-public-offering-of-common', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/509/pieris-pharmaceuticals-strenghtens-senior-management-team', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/500/pieris-pharmaceuticals-to-present-data-on-novel-anti-cd137', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/506/pieris-pharmaceuticals-to-host-second-quarter-2015-investor', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/501/pieris-pharmaceuticals-completes-dosing-of-healthy', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/496/pieris-pharmaceuticals-to-present-at-the-2015-ubs-global', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/495/pieris-pharmaceuticals-to-host-first-quarter-2015-investor', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/499/pieris-pharmaceuticals-appoints-immuno-oncology-expert', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/498/pieris-pharmaceuticals-reports-first-quarter-2015-financial', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/484/pieris-pharmaceuticals-reports-full-year-2014-financial', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/497/pieris-pharmaceuticals-appoints-former-celgene-and-sanofi', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/494/pieris-pharmaceuticals-and-the-university-of-melbourne', 'http://www.pieris-ag.com/news-and-events/press-releases/detail/464/pieris-pharmaceuticals-to-host-fiscal-2014-results-call', 'https://www.wowtechnologies.com/success-stories', 'https://www.wowtechnologies.com/success-stories?lightbox=dataItem-ihnuz24b', 'https://www.wowtechnologies.com/success-stories?lightbox=dataItem-ihnuz24c', 'https://www.wowtechnologies.com/success-stories?lightbox=dataItem-ihnuz24d3', 'http://www.novartis.com/our-company/board-directors', 'http://www.novartis.com/news/stay-date', 'http://www.novartis.com/news/stay-up-to-date', 'http://www.novartis.com/tags/drug-discovery', 'https://www.novartis.com/our-company/board-directors', 'http://www.novartis.com/news/media-releases/novartis-enters-agreement-acquire-avexis-inc-usd-87-bn-transform-care-sma-and-expand-position-gene-therapy-and-neuroscience-leader', 'http://www.novartis.com/news/media-releases/sandoz-outlines-plans-next-healthcare-access-challenge-hack-support-local-digital-innovation', 'https://www.novartis.com/news/novartis-corporate-fact-sheet', 'https://www.novartis.com/news/stay-up-to-date', 'http://www.novartis.com/news/media-releases/novartis-present-predictability-data-brolucizumab-namd-from-pivotal-hawk-and-harrier-trials-arvo', 'https://www.novartis.com/news/novartis-2017-financial-results', 'https://www.novartis.com/news/media-releases/novartis-shareholders-approve-all-resolutions-proposed-board-directors', 'https://www.novartis.com/news/media-releases/primary-analysis-results-from-novartis-pivotal-juliet-trial-show-kymriahtm-tisagenlecleucel-sustained-complete-responses-six-months-adults-rr-dlbcl-difficult', 'https://www.novartis.com/news/media-releases/novartis-highlights-its-strong-foundation-long-term-sustainable-growth-third', 'https://www.novartis.com/news/media-releases/novartis-shareholders-approve-all-resolutions-proposed-board-directors-annual', 'https://www.novartis.com/news/media-releases/novartis-drug-crizanlizumab-shown-prolong-time-patients-first-sickle-cell-pain-crisis-subgroup-analysis-sustain-study', 'https://www.novartis.com/news/media-releases/novartis-kisqalir-first-and-only-cdk46-inhibitor-show-superior-median-pfs-compared-oral-endocrine-therapy-first-line-treatment-prospective-randomized-phase-iii', 'https://www.novartis.com/news/media-releases/novartis-highlights-its-differentiated-late-stage-pipeline-rd-update-and', 'https://www.novartis.com/news/media-releases/meet-novartis-management-investor-event-novartis-highlights-focus-innovation-and', 'http://www.novartis.com/news/novartis-corporate-fact-sheet', 'https://www.novartis.com/news/media-releases/novartis-and-max-foundation-transform-pioneering-cancer-access-program-people', 'https://www.novartis.com/news/media-releases/novartis-ascp-and-acs-join-forces-fight-cancer-ethiopia-uganda-and-tanzania', 'http://www.novartis.com/tags/medical-innovations', 'http://www.novartis.com/tags/drug-development', 'https://www.novartis.com/tags/drug-discovery', 'https://www.novartis.com/news/media-releases/novartis-teams-harvard-develop-next-generation-biomaterial-systems-deliver-immunotherapies', 'http://www.novartis.com/tags/drug-discovery?page=1', 'http://www.novartis.com/tags/drug-discovery?page=4', 'http://www.novartis.com/tags/drug-discovery?page=3', 'http://www.novartis.com/tags/drug-discovery?page=2', 'https://www.novartis.com/news/media-releases/novartis-shareholders-approve-all-resolutions-proposed-board-directors-annual-general-meeting', 'https://www.novartis.com/news/media-releases/novartis-improves-ranking-2016-access-medicine-index', 'http://www.novartis.com/our-focus/cancer/oncology-disease-areas/soft-tissue-sarcoma', 'http://www.novartis.com/news/novartis-corporate-fact-sheet#tab-3', 'http://www.novartis.com/news/novartis-corporate-fact-sheet#tab-1', 'http://www.novartis.com/news/novartis-corporate-fact-sheet#tab-2', 'https://www.novartis.com/news/media-releases/novartis-reports-over-half-psoriasis-patients-do-not-reach-achievable-treatment', 'http://www.novartis.com/our-company/corporate-responsibility/doing-business-responsibly/health-safety-environment/environmental-sustainability/water-micro-pollutants', 'https://www.novartis.com/news/contributing-breath-fresh-air-zambian-health-care', 'http://www.novartis.com/tags/drug-design', 'https://www.novartis.com/news/stay-date', 'http://www.novartis.com/tags/medical-innovations?page=1', 'https://www.novartis.com/tags/medical-innovations', 'https://www.novartis.com/tags/drug-development', 'https://www.novartis.com/news/nurturing-next-generation-scientists', 'https://www.novartis.com/news/media-releases/novartis-enters-agreement-acquire-avexis-inc-usd-87-bn-transform-care-sma-and-expand-position-gene-therapy-and-neuroscience-leader', 'https://www.novartis.com/news/media-releases/sandoz-outlines-plans-next-healthcare-access-challenge-hack-support-local-digital-innovation', 'http://www.novartis.com/news/media-releases', 'https://www.novartis.com/news/novartis-corporate-fact-sheet#tab-2', 'https://www.novartis.com/news/novartis-corporate-fact-sheet#tab-3', 'https://www.novartis.com/news/media-releases/novartis-present-predictability-data-brolucizumab-namd-from-pivotal-hawk-and-harrier-trials-arvo', 'https://www.novartis.com/our-company/corporate-responsibility/doing-business-responsibly/health-safety-environment/environmental-sustainability/water-micro-pollutants', 'https://www.novartis.com/tags/drug-design', 'https://www.novartis.com/news/media-releases/kenya-first-country-launch-novartis-access-expanding-affordable-treatment', 'https://www.novartis.com/our-focus/cancer/oncology-disease-areas/soft-tissue-sarcoma', 'http://www.novartis.com/news/media-releases/novartis-teams-harvard-develop-next-generation-biomaterial-systems-deliver-immunotherapies', 'http://www.novartis.com/news/media-releases/phase-iii-data-lancet-show-novartis-siponimod-significantly-improves-outcomes-patients-secondary-progressive-ms', 'http://www.novartis.com/news/media-releases/sandoz-receives-positive-chmp-opinion-proposed-biosimilar-infliximab', 'http://www.novartis.com/news/media-releases/novartis-announces-changes-executive-committee-support-strategic-priorities', 'http://www.novartis.com/news/media-releases/novartis-drug-tasignar-approved-fda-treat-children-rare-form-leukemia', 'http://www.novartis.com/news/media-releases/novartis-sell-stake-consumer-healthcare-joint-venture-gsk-usd130-billion-focus-strategic-priorities', 'https://www.novartis.com/news/severity-psoriasis', 'https://www.novartis.com/news/acute-heart-failure-symptoms-and-treatments', 'https://www.novartis.com/news/media-releases/kae609-shows-promise-next-generation-treatment-malaria', 'https://www.novartis.com/news/media-releases/phase-iii-data-lancet-show-novartis-siponimod-significantly-improves-outcomes-patients-secondary-progressive-ms', 'https://www.novartis.com/news/media-releases/sandoz-receives-positive-chmp-opinion-proposed-biosimilar-infliximab', 'https://www.novartis.com/news/media-releases/novartis-announces-changes-executive-committee-support-strategic-priorities', 'https://www.novartis.com/news/media-releases/novartis-drug-tasignar-approved-fda-treat-children-rare-form-leukemia', 'https://www.novartis.com/news/media-releases/novartis-sell-stake-consumer-healthcare-joint-venture-gsk-usd130-billion-focus-strategic-priorities', 'http://www.nordicbioscience.com', 'http://www.nordicbioscience.com/', 'http://www.nordicbioscience.com/#', 'http://www.nordicbioscience.com/#27', 'http://www.nordicbioscience.com/#15', 'http://www.nordicbioscience.com/#11;12', 'http://www.nordicbioscience.com/#17', 'http://www.nordicbioscience.com/#14', 'http://www.nordicbioscience.com/#19;22', 'http://www.nordicbioscience.com/#34;35', 'http://www.nordicbioscience.com/#38', 'http://www.nordicbioscience.com/#26', 'http://www.nordicbioscience.com/#2', 'http://www.nordicbioscience.com/#40', 'http://www.nordicbioscience.com/#7', 'http://www.nordicbioscience.com/#13', 'http://www.nordicbioscience.com/#45', 'http://www.nordicbioscience.com/#32;33', 'http://www.nordicbioscience.com/#42', 'http://www.nordicbioscience.com/#23;24', 'http://www.nordicbioscience.com/#/', 'http://www.nordicbioscience.com/#18', 'http://www.nordicbioscience.com/#31', 'http://www.nordicbioscience.com/#41', 'http://www.nordicbioscience.com/#24', 'http://www.nordicbioscience.com/#1', 'http://www.nordicbioscience.com/#4', 'http://www.nordicbioscience.com/#29', 'http://www.nordicbioscience.com/#10', 'http://www.nordicbioscience.com/#36', 'http://www.nordicbioscience.com/#28', 'http://www.nordicbioscience.com/#8;9', 'http://www.nordicbioscience.com/#43', 'http://www.nordicbioscience.com/#30', 'http://www.nordicbioscience.com/#25', 'http://www.nordicbioscience.com/#3', 'http://www.nordicbioscience.com/#20', 'http://www.nordicbioscience.com/#37', 'http://www.nordicbioscience.com/#5', 'http://www.nordicbioscience.com/#44', 'http://www.nordicbioscience.com/#39']]
#%%
import json
with open(r'C:\Users\g.rozenaite\Desktop\D4I_companies_summary.txt', 'w') as outfile:
    json.dump(dictorelis, outfile)