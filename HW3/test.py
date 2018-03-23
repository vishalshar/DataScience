from collections import Counter
from nltk.tokenize import RegexpTokenizer


d1 = {'a':2,'b':3,'d':5}
d2 = {'a':2,'b':3,'d':5,'e':3}

d3 = ['a','a','a','b','b','b','c','c','c']
d4 = ['a','a','a','b','b','b','c','c','c','d','d','d']
d5 = Counter(d3) + Counter(d4)
print d5

tokenizer = RegexpTokenizer(r'\w+')


bio = "a vd erwg wert wert wert wqert"
bio = tokenizer.tokenize(bio)
bio = [word for word in bio if len(word) > 2]
print bio