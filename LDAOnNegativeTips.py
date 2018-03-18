# -*- coding: utf-8 -*-
from nltk.tokenize import RegexpTokenizer
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from collections import Counter
import timeit
import csv
import re
import json
import time
import pickle
from multiprocessing.dummy import Pool as ThreadPool
import sys
from gensim import corpora, models

reload(sys)
sys.setdefaultencoding("utf-8")

snowball_stemmer = SnowballStemmer('english')
tokenizer = RegexpTokenizer(r'\w+')
stops = set(stopwords.words("english"))
wordnet_lemmatizer = WordNetLemmatizer()


negativeTipsFile = "./fastFoodNegativeReviews.txt"


def clean(line):
    text = line
    text = re.sub("[^a-zA-Z]", " ", text)
    text = text.lower()
    text = tokenizer.tokenize(text)
    text = [w for w in text if not w in stops]
    # text = [snowball_stemmer.stem(word) for word in text]
    text = [wordnet_lemmatizer.lemmatize(word) for word in text]
    text = [word for word in text if len(word) > 3]
    # print text
    return text

cleanData = []
with open(negativeTipsFile) as infile:
    negativeTips = infile.readlines()
    print 'Reading file'
    for line in negativeTips:
        cleanData.append(clean(line))
# print cleanData
print 'Corpus to Term Matrix'
# Document to term matrix
print type(cleanData)
print len(cleanData)
dictionary = corpora.Dictionary(cleanData)
print dictionary
corpus = [dictionary.doc2bow(text) for text in cleanData]
print(corpus[0])
print 'Building Models'
ldamodel = models.ldamodel.LdaModel(corpus, num_topics=10, id2word=dictionary, passes=100)
print(ldamodel.print_topics(num_topics=10, num_words=10))




