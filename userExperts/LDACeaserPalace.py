from nltk.tokenize import RegexpTokenizer
import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models


snowball_stemmer = SnowballStemmer('english')
tokenizer = RegexpTokenizer(r'\w+')
stops = set(stopwords.words("english"))
wordnet_lemmatizer = WordNetLemmatizer()

def clean(line):
    text = line
    text = re.sub("[^a-zA-Z0-9]", " ", text)
    text = text.lower()
    text = tokenizer.tokenize(text)
    text = [w for w in text if not w in stops]
    # text = [snowball_stemmer.stem(word) for word in text]
    text = [wordnet_lemmatizer.lemmatize(word) for word in text]
    text = [word for word in text if len(word) > 3]
    # print text
    return text



listOfReviews = ''
with open('./negativeReviewsCeaserPalace.json', 'rb') as f:
    for line in f:
        listOfReviews = line

# print listOfReviews
print type(listOfReviews)
print len(listOfReviews)
# print listOfReviews
listOfReviews = listOfReviews.split(",")

cleanData = []
for line in listOfReviews:
    cleanData.append(clean(line))
# print listOfReviews
# print type(listOfReviews)
# print len(listOfReviews)
# print listOfReviews
print 'Corpus to Term Matrix'
# Document to term matrix
dictionary = corpora.Dictionary(cleanData)
print dictionary
corpus = [dictionary.doc2bow(text) for text in cleanData]
print(corpus[0])
print 'Building Models'
ldamodel = models.ldamodel.LdaModel(corpus, num_topics=10, id2word=dictionary, passes=100)
print(ldamodel.print_topics(num_topics=10, num_words=10))
