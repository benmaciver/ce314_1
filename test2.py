import nltk
from nltk import bigrams, FreqDist

#helper function
def is_punctuation(char):
    return char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


#question 1
print("Question 1:")
#Get corpus
reuters = nltk.corpus.reuters.words()

#Clean and prepare corpus
filtered_content=[]
for word in reuters:
    if word[0] != word[-1]:
        filtered_content.append(word.lower())
    elif is_punctuation(word[0])!= True:
        filtered_content.append(word.lower())

#Create bigrams and get frequency distribution  
bigrams = bigrams(filtered_content)
bigram_frequencies = FreqDist(bigrams)

total_bigrams = bigram_frequencies.N()
print(total_bigrams)
bigram_probabilities ={}

for bigram,frequency in bigram_frequencies.items():
    bigram_probabilities[bigram] = int(frequency)/total_bigrams


#question 2
print("Question 2:")
next_word = ""
highest_prob = -1
for bigram,probability in bigram_probabilities.items():
    #print(probability)
    if bigram[0] == "is" and probability > highest_prob:
        highest_prob = probability
        next_word = bigram[1]

if (next_word == ""):
    print ("no next word")
else:
    print (f"Next word following 'He is {next_word}'") 


#question3
print("Question 3:")

    


