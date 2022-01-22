# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 01:16:29 2018

@author: Keshav
"""

from nltk.book import *
from nltk.corpus import gutenberg as g
from nltk.corpus import brown as b
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader as t
from math import *

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps = PorterStemmer()

def cv(a):
        vowels = ["a", "e", "i", "o", "u"]
        vowel = False
        for vowell in vowels:
                if vowell in a:
                        vowel = True
        return vowel
    
stop=set(stopwords.words('english'))

c=b.categories()

w=[]
for i in c:
    w=w+b.words(categories=i)
        
wo=set(x.lower() for x in w if cv(x)==True )
totw=len(wo)


fd=[]
l=[]
w=[]
for j in c:
    w=b.words(categories=j)
    w1=sorted(x.lower() for x in w if cv(x)==True)
    l.append(len(set(w1)))
    wf=FreqDist(w1)
    fd.append(wf)
    

fdir = "M://Personal//NLP//Spyder//Classify"
wl=t(fdir,".*")
f=wl.fileids()

wt=wl.words('religious.txt')
tc=sorted(x.lower() for x in wt if cv(x)==True)


plist=[]
for i in range(len(fd)):
    p=0
    for j in tc:
        k=log((fd[i][j]+1)/(l[i]+total),20)
        p=p+k
    plist.append(p)
      
print(c[plist.index(max(plist))])
    





