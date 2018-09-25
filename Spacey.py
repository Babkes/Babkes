# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 16:26:46 2018

@author: g.rozenaite
"""
import spacy
spacy.load('en')

flatten = lambda l: [item for sublist in l for item in sublist]
words_list_bad = flatten(map((lambda x: x.split(" ")), file_bad_split))
words_list_good = flatten(map((lambda x: x.split(" ")), file_good_split))
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

#%%
import spacy
import pandas as pd
import pickle
nlp =  spacy.load('en')
df = pd.read_excel(r"C:\Users\g.rozenaite\Desktop\Link galutinio produkto.xlsx",
                       sheet_name='Testuojam SpaCy')
texty = df['text'].values.tolist()
file = open(r"C:\Users\g.rozenaite\Desktop\name_dift.pkl", "rb")
dict = pickle.load(file)
for text in texty:
    text = nlp(text)
    for token in text:
        print (token)
#%% print (token, token.dep, token.pos, token.pos_)
with open("bad_emails.txt") as file:
    file_bad_read = file.read()
    file_bad_split = file_bad_read.split("\r\n")

with open("good_emails.txt") as file:
    file_good_read = file.read()
    file_good_split = file_good_read.split("\r\n")