# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:37:24 2018

@author: g.rozenaite
"""

#%%
import pickle
import pandas as pd
file = open (r"C:\Users\g.rozenaite\Desktop\nace2.pkl", "rb")
nace = pickle.load(file)
df = pd.DataFrame.from_dict(nace, orient='index')
df_t = df.transpose()
writer = pd.ExcelWriter(r"C:\Users\g.rozenaite\Desktop\nace2.xlsx")
df_t.to_excel(writer, sheet_name = 'nace')
print (df)
#%%
import pandas as pd
import pickle
df = pd.read_excel(r"C:\Users\g.rozenaite\Desktop\nace3.xlsx", 
                         sheet_name = 'nace')
dict = df.set_index('nace').to_dict(orient = 'list')
f = open(r"C:\Users\g.rozenaite\Desktop\nace3.pkl","wb")
pickle.dump(dict,f)
f.close()
#%%
import pickle
file = open(r"C:\Users\g.rozenaite\Desktop\rich_text.pkl", "rb")
richy = pickle.load(file)
#%%
import pickle
import pandas as pd
df_l = pd.read_excel(r'C:\Users\g.rozenaite\Documents\Darbai\Viskas su DATA\Innovation language.xlsx',
                     sheet_name = 'Mega version_TS')
dict_l = df_l.set_index('Kategorija').transpose().to_dict(orient = 'list')
print(dict_l)
f = open(r"C:\Users\g.rozenaite\Desktop\StageZodynas.pkl","wb")
pickle.dump(dict_l,f)
f.close()
   