# -*- coding: utf-8 -*-
"""
Created on Tue May  8 11:15:55 2018

@author: Keshav
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 09:54:35 2018

@author: Keshav
"""
from __future__ import division
from nltk.book import *
from nltk.corpus import brown as b
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader as t
from math import *

def cv(a):
        vowels = ["a", "e", "i", "o", "u"]
        vowel = False
        for vowell in vowels:
                if vowell in a:
                        vowel = True
        return vowel

stop=set(stopwords.words('english'))
c=b.categories()


c=['religion','romance','news']
w=[]
for i in c:
    w=w+b.words(categories=i)
        
wo=set(x.lower() for x in w if(cv(x)==True and x not in stop))
totw=len(wo)


fd=[]
l=[]
w=[]
for j in c:
    w=b.words(categories=j)
    w1=sorted(x.lower() for x in w if(cv(x)==True and x not in stop))
    l.append(len(set(w1)))
    wf=FreqDist(w1)
    fd.append(wf)
    

fdir = "M://Personal//NLP//Project Shown//NLP//Classify"
wl=t(fdir,".*")
f=wl.fileids()

wt=wl.words('romantic.txt')
tc=sorted(x.lower() for x in wt if( cv(x)==True and x not in stop))

#tc="I like to pray to god"
#tc=tc.split()

plist=[]

for i in range(len(fd)):
    p=0
    for j in tc:
        k=log(((fd[i][j]+1)/(l[i]+totw)), 20)
        p=p+k
    plist.append(p)
      
print('\n Category is :-',c[plist.index(max(plist))])     
