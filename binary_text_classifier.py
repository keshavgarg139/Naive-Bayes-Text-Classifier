# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 09:54:35 2018

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
#wlist=[]
#c1=['romance',]
#for i in c:
#    w=b.words(categories='romance')
#    w1=sorted(list(set(x.lower() for x in w if(x not in stop and cv(x)==True))))
#    wf=FreqDist(w1)


w=b.words(categories='romance')
w1=sorted(x.lower() for x in w if cv(x)==True )    
wf1=FreqDist(w1)
l1=len(set(w1))

w=b.words(categories='religion')
w2=sorted(x.lower() for x in w if cv(x)==True)     
wf2=FreqDist(w2)
l2=len(set(w2))

total=len(set(w1+w2))

fd = "M://Personal//NLP//Spyder//Classify"
wl=t(fd,".*")
f=wl.fileids()

wt1=wl.words('religious.txt')
tc=sorted(list(set(x.lower() for x in wt1 if cv(x)==True))) 

p1=0;
p2=0;

for i in tc:
    p1=p1+log((wf1[i]+1)/(l1+total),20)
    p2=p2+log((wf2[i]+1)/(l2+total),20)
        

wt2=wl.words('romantic.txt')
print(wt2)
tc2=sorted(list(set(x.lower() for x in wt2 if(x not in stop and cv(x)==True))))   

p12=1;
p22=1;
for i in tc2:
    if i in w1:
        p12=p12*wf1.freq(i)
        
    if i in w2:
        p22=p22*wf2.freq(i)
       
    
    