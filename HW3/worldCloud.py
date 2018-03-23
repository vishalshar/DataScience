import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from collections import Counter
import timeit
import csv
import re
import json
import time
import pickle
from multiprocessing.dummy import Pool as ThreadPool

listWords = {}
stops = set(stopwords.words("english"))
# pool = ThreadPool(6)

times = 0
count = 0
# Snowball stemmer and wordNet Lemmatizer
snowball_stemmer = SnowballStemmer('english')
wordnet_lemmatizer = WordNetLemmatizer()


def clean(line):
    text = line[0]
    text = re.sub("[^a-zA-Z]", " ", text)
    text = text.lower().split()
    text = [w for w in text if not w in stops]
    text = [snowball_stemmer.stem(word) for word in text]
    text = [wordnet_lemmatizer.lemmatize(word) for word in text]
    return text


with open("./negativeTips.txt") as infile:
    reader = csv.reader(infile)
    # listWords = pool.map(clean, reader) #Mapper built in for Python are like multithreading rather than Map-Reducer
    start_time = time.time()
    for line in reader:
        for word in clean(line):
            if word in listWords:
                listWords[word] += 1
            else:
                listWords[word] = 1
        count += 1
        if count >= 100000:
            print times, count, (time.time() - start_time)
            start_time = time.time()
            count = 0
            times += 1

# json.dump(listWords, open("./file.txt",'w'))

with open('./dictNegativeTips.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in listWords.items():
        writer.writerow([key, value])


