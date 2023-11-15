#import nltk, re, pprint, string
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import reuters
from nltk.util import ngrams
from nltk.corpus import stopwords

corpus = reuters.words()
words = word_tokenize(corpus)
stop_words = set(stopwords.words('english'))
        
for word in words:
    if word not in stop_words:
        filtered_words.append(word)

print(filtered_words)
