# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 03:07:37 2018

@author: Keshav
"""

from sklearn.datasets import fetch_20newsgroups
news = fetch_20newsgroups(subset='all')

from nltk.book import *
from nltk.corpus import gutenberg as g
from nltk.corpus import brown as b
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader as t
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps = PorterStemmer()

c=b.categories()

raw=[]
target=[]

for i in c:
    fid=b.fileids(i)
    for j in fid:
        s=b.raw(j)
        raw.append(s)
        target.append(i)


from sklearn.cross_validation import train_test_split
 
def train(classifier, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
 
    classifier.fit(X_train, y_train)
    print ("Accuracy: %s" % classifier.score(X_test, y_test))
    return (classifier)

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
 
trial1 = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', MultinomialNB()),
])
 
train(trial1, raw , target)

from nltk.corpus import stopwords
 
trial2 = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words=stopwords.words('english'))),
    ('classifier', MultinomialNB()),
])

train(trial2, raw , target)

import string
from nltk.stem import PorterStemmer
from nltk import word_tokenize
 
def stemming_tokenizer(text):
    stemmer = PorterStemmer()
    return [stemmer.stem(w) for w in word_tokenize(text)]
 
trial5 = Pipeline([
    ('vectorizer', TfidfVectorizer(tokenizer=stemming_tokenizer,
                             stop_words=stopwords.words('english') + list(string.punctuation))),
    ('classifier', MultinomialNB(alpha=0.05)),
])    

train(trial5, raw , target)

