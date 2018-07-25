import pandas as pd
from googleapiclient.discovery import build
names_df = pd.read_excel(r"C:\Users\g.rozenaite\Desktop\Galutinis produktas.xlsx"
                         , sheet_name = 'Pradzia')
keywords = names_df['name'].values.tolist()
url_df = pd.DataFrame([])
api_key = "AIzaSyB9KBuW01lIrnk8PoIbyntZAdpQkB4iD54"
cse_id = "007703736530656354066:2sgdezn3w2e"
def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        results = service.cse().list(q = search_term, cx=cse_id, **kwargs).execute()
        if ('items') in results:
            return results ['items'] 
        else:
            print (i + ' ' + 'No Results, good luck next time!')
for i in keywords[3201:]:
    results1 = google_search(i, api_key, cse_id, num=10)
    if results1 != None:
        for result in results1:
            url_df = url_df.append(pd.DataFrame(
                    {'name': [i], 'url': [result['link']], 
                     'snippet': [result['snippet']]},
                    index=[0]), ignore_index=True)
    results2 = google_search(i, api_key, cse_id, num=10, start = 11)
    if results2 != None:
        for result in results2:
            url_df = url_df.append(pd.DataFrame(
                    {'name': [i], 'url': [result['link']], 
                     'snippet': [result['snippet']]},
                    index=[0]), ignore_index=True)
mergerisdf = pd.merge(names_df [['id','name']],
                url_df[['name', 'url', 'snippet']],
                 on=['name'], 
                 how='left')
mergerisexc = pd.ExcelWriter('Links.xlsx')
mergerisdf.to_excel(mergerisexc, 'Antras žingsnis')
mergerisexc.save()
