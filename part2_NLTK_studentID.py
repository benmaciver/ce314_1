 #requires user to call nltk.download() in the shell first and download book

import nltk
from nltk.book import text7
from collections import Counter

wsj =[]
wsj = text7.tokens

wordCounts = Counter(wsj)

mostCommon = wordCounts.most_common(50)
i = 1;
for string,count in mostCommon:
    print(f"{i}){string}")
    i+=1
