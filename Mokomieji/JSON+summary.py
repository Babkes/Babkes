
# coding: utf-8

# In[1]:


import pyodbc
import pickle
import pandas as pd


# In[99]:


# load data
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=WINSRV;"
                      "Database=Data4Impact;"
                      "Trusted_Connection=yes;")
cursor = cnxn.cursor()
query="SELECT DISTINCT company_id  FROM FP7_HEALTH"
df_data = pd.read_sql(query,cnxn)
list_data = df_data['company_id'].values.tolist()


# In[74]:


df_data


# In[75]:


df_company = pd.DataFrame(columns = ['innovation?', 'tangible + pre_market', 'tangible + market',
                                     'intangible + pre_market', 'intangible + market'])
names = pd.read_excel(r'C:\Users\g.rozenaite\Desktop\Pradzia.xlsx')
df_company['PIC'] = names['id']


# In[102]:


df_company


# In[103]:


df_company2 = pd.DataFrame([])
for i, row in df_company.iterrows():
    if row['PIC'] in list_data:
        x = 'Yes'
        print (x)
    else:    
        x = 'No'
    df_company2 = df_company2.append(pd.DataFrame({'company_id': [row['PIC']], 'data gathered?': [x],
        'tangible + pre_market': [0], 'tangible + market': [0], 'intangible + pre_market':[0], 'intangible + market': [0]},
                    index=[0]), ignore_index=True)        


# In[104]:


df_company2


# In[109]:


cursor = cnxn.cursor()
query="SELECT DISTINCT company_id  FROM FP7_HEALTH WHERE prediction = 1"
df_prediction = pd.read_sql(query,cnxn)
list_prediction = df_prediction['prediction'].values.tolist()


# In[110]:


df_prediction


# In[111]:


list_prediction = df_prediction['company_id'].values.tolist()


# In[112]:


df_company3 = pd.DataFrame([])
for i, row in df_company2.iterrows():
    if row['data gathered?'] == 'Yes':
        if row['company_id'] in list_prediction:
            x = '1'
            print (x)
        else:
            x = 0
            print (x)
    else:
        x = 'Na'
        print (x)
    df_company3 = df_company3.append(pd.DataFrame({'company_id': row['company_id'], 'innovation?': [x]},
                                                  index = [0]), ignore_index = True)


# In[113]:


df_company3


# In[115]:


galutine_df = pd.merge(df_company2[['company_id', 'data gathered?', 'tangible + pre_market', 'tangible + market',
                   'intangible + pre_market', 'intangible + market']], df_company3[['company_id', 'innovation?']],
                        on = ['company_id'], how = 'left')


# In[116]:


galutine_df


# In[117]:


galutine_df ['PIC'] = galutine_df['company_id']
galas =  galutine_df.drop('company_id', 1)
gaunasi = galas.drop_duplicates(subset = 'PIC')
gana = gaunasi.set_index('PIC')


# In[118]:


gana


# In[119]:


dictorelis = gana.to_dict ('index')


# In[123]:


dictorelis


# In[121]:


import json


# In[122]:


with open(r'C:\Users\g.rozenaite\Desktop\D4I_companies_summary.txt', 'w') as outfile:
    json.dump(dictorelis, outfile)

