import nltk
from nltk import bigrams, FreqDist

#helper functions
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

#saves total number of bigrams
total_bigrams = bigram_frequencies.N()
#gets the probability of each bigram by dividing its frequency by total bigrams
bigram_probabilities ={}
for bigram,frequency in bigram_frequencies.items():
    bigram_probabilities[bigram] = int(frequency)/total_bigrams


#question 2
print("Question 2:")
next_word = ""
highest_prob = -1
#iterates through bigram probabilities searching for bigram that begins with "is" and saves one of highest probability
for bigram,probability in bigram_probabilities.items():
    if bigram[0] == "is" and probability > highest_prob:
        highest_prob = probability
        next_word = bigram[1]
#search failed for some reason (has never been true in my testing)
if (next_word == ""):
    print ("no next word")
else:
    print (f"Next word predicition has produced... 'He is {next_word}'") 


#question3
print("Question 3:")   
sentence = "he is" 
last_word = "is"
#repeats previous for loop 5 times to get a full sentence
for x in range (5):
    next_word = ""
    highest_prob = -1
    #same as before but last_word changes each iteration to reflect the latest word added to the sentence
    for bigram,probability in bigram_probabilities.items():
        if bigram[0] == last_word and probability > highest_prob:
            highest_prob = probability
            next_word = bigram[1]
    sentence+= f" {next_word}"#new word added to sentence
    last_word = next_word#last word changed
print(sentence+".")
