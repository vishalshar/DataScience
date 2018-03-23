import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
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
pool = ThreadPool(10)

times = 0
count = 0
# Snowball stemmer and wordNet Lemmatizer
snowball_stemmer = SnowballStemmer('english')
wordnet_lemmatizer = WordNetLemmatizer()
sentimentVanderAnalyzer = SentimentIntensityAnalyzer()
wordnet_lemmatizer = WordNetLemmatizer()


def sentimentAnalyzer(line):
    global count
    global times
    count += 1
    res = {"greater": 0, "less": 0, "equal": 0}
    sentimentScore = sentimentVanderAnalyzer.polarity_scores(line)
    if sentimentScore["compound"] == 0.0:
        res["equal"] += 1
    elif sentimentScore["compound"] > 0.0:
        res["greater"] += 1
    else:
        res["less"] += 1
    print res
    with open('./dictNegativeReviewsFastFood.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(line)
    if count >= 100000:
        print times, count,
        count = 0
        times += 1
    return


with open("./negativeTips.txt") as infile:
    reader = csv.reader(infile)
    # Mapper built in for Python are like multithreading rather than Map-Reducer
    # pool.map(sentimentAnalyzer, reader)
    sentimentAnalyzer("Mr Hoagie is an institution. Walking in, it does seem like a throwback to 30 years ago, old fashioned menu board, booths out of the 70s, and a large selection of food. Their speciality is the Italian Hoagie, and it is voted the best in the area year after year. I usually order the burger, while the patties are obviously cooked from frozen, all of the other ingredients are very fresh. Overall, its a good alternative to Subway, which is down the road.")
