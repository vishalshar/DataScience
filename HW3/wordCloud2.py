import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from unidecode import unidecode
import collections
import timeit
import csv
import re
import collections
import operator
import pickle
from multiprocessing.dummy import Pool as ThreadPool
import wordcloud

result = []
count = 0
# pool = ThreadPool(4)


def count(line):
    line = line.split(",")
    formatted = []
    for data in line:
        formatted.append(re.sub("[^a-zA-Z]", " ", data).strip())
    return collections.Counter(formatted).items()

c = 0
dict = {}
# with open("/home/vishal/Downloads/yelp_dataset_challenge_academic_dataset/results.csv") as infile:
with open("./file.txt") as infile:
    line = infile.readlines()
    print len(line[0])
    print type(line[0])
    line = line[0].replace("{","")
    line = line.replace("}", "")
    line = line.split(",")
    for word in line:
        data = word.split(":")
        dict[data[0].strip().replace("\"","").replace("\"","")] = data[1].strip()

freq = []
for value in dict.values():
    freq.append(int(value))
sorted_freq = sorted(freq,reverse=True)

for fre in sorted_freq[:200]:
    print fre

