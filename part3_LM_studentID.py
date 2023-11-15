import nltk
from nltk import word_tokenize
from nltk import tokenize
from nltk.util import ngrams
from nltk.corpus import reuters
from nltk import bigrams, FreqDist
from nltk.corpus import stopwords


stop_words = set(stopwords.words('english'))

words = reuters.words()#tokenizes rueters corpus
filtered_words =[]
for word in words:
    if word not in stop_words:
        filtered_words.append(word)
        
    

#gets a list of all the bigrams and then uses FreqDist to determine the frequencey of each unique bigram and creates a dictionary of this info
bigrams = bigrams(filtered_words)
bigram_model = FreqDist(bigrams)


token = word_tokenize("he is")
ngram = {1: [], 2: []}

for i in range(3):
    ngrams_list = list(ngrams(token, i + 1))
    if ngrams_list:
        ngram[i + 1] = ngrams_list[-1]

print(ngram)
next_word=''
highestFreq =0
for bigram,freq in bigram_model:
    if bigram[1] == "is" and freq > highestFreq:
        next_word = bigram[2]
print(next_word)
print(bigram_model.predict("he is"))
        
    
    




