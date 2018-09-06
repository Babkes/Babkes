# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 16:26:46 2018

@author: g.rozenaite
"""
import spacy
import pandas as pd
import pickle
import random
from pathlib import Path
from __future__ import unicode_literals, print_function
nlp =  spacy.load('en')
df = pd.read_excel(r"C:\Users\g.rozenaite\Desktop\Link galutinio produkto.xlsx",
                       sheet_name='Testuojam SpaCy')
texty = df['text'].fillna('no').values.tolist()
file = open(r"C:\Users\g.rozenaite\Desktop\name_dict.pkl", "rb")
train_data = pickle.load(file)
#dict = file.tolist()
for text in file:
    text = nlp(text)
    for token in text:
        print (token, token.pos_)
#%% NER

#%%
file = open(r"C:\Users\g.rozenaite\Desktop\name_dict.pkl", "rb")
file = pickle.load(file)
train_data = list(file.keys())
#%%
train_data = [
     ("Uber blew through $1 million a week", {'entities': [(0, 4, 'ORG')]}),
     ("Google rebrands its business apps", {'entities': [(0, 6, "ORG")]})]
nlp = spacy.blank('en')
optimizer = nlp.begin_training()
VECTORS_KEY = 'spacy_pretrained_vectors'
def link_vectors_to_models(vocab):
    vectors = vocab.vectors
    if vectors.name is None:
        vectors.name = VECTORS_KEY
        print(
        "Warning: Unnamed vectors -- this won't allow multiple vectors "
        "models to be loaded. (Shape: (%d, %d))" % vectors.data.shape)
for i in range(20):
    random.shuffle(train_data)
    for text, annotations in train_data:
        nlp.update([text], [annotations], sgd=optimizer)
nlp.to_disk('/model')


#%% print (token, token.dep, token.pos, token.pos_)
with open("bad_emails.txt") as file:
    file_bad_read = file.read()
    file_bad_split = file_bad_read.split("\r\n")

with open("good_emails.txt") as file:
    file_good_read = file.read()
    file_good_split = file_good_read.split("\r\n")
flatten = lambda l: [item for sublist in l for item in sublist]
words_list_bad = flatten(map((lambda x: x.split(" ")), file_bad_split))
words_list_good = flatten(map((lambda x: x.split(" ")), file_good_split))

#%%
import pandas as pd
df = pd.DataFrame(({'country' : ['AT', 'ATFEB', 'BE', 'BG', 'CYC', 'CZ', 'DE',
'DK', 'EE', 'ESA', 'FI', 'FR', 'GB', 'GBNI', 'GBSC', 'HR', 'HU', 'IE', 'IT', 
'LT', 'NL', 'PL', 'PT', 'RO', 'SE', 'SI','SK'], 
'share': [0.0333333, 0, 0.2291667, 0.3632653, 0.7094972, 0.259542, 
0.2485549, 0.2407407, 0.0776699, 0, 0.4435484, 0.5257353, 0.5690608, 0, 0.5, 0.3012048, 0.1, 0, 0, 0, 0, 0, 0.8055556,
0.0588235, 0.2153846, 0.5945946, 0.3571429, 0.6], 
'n': [60, 2, 48, 245, 179, 131, 173, 216, 103, 1, 124, 272, 362, 7, 8, 
166, 100, 48, 68, 14, 25, 19, 36, 51, 130, 74, 28, 15]}, index=[0]), ignore_index = True)
print (df)

#%%
import csv
import random
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
                # as theres 4 columns
	            dataset[x][y] = float(dataset[x][y])
                # converts numbers from string to float
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])

trainingSet=[]
testSet=[]
loadDataset('iris.data', 0.66, trainingSet, testSet)
print(trainingSet)
print(testSet)
print('Train: ' + repr(len(trainingSet)))
print('Test: ' + repr(len(testSet)))