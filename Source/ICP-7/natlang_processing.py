import requests
from bs4 import BeautifulSoup
import nltk
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk import trigrams
from nltk import wordpunct_tokenize, ne_chunk, pos_tag

# Get URL and parse the page
url = requests.get('https://en.wikipedia.org/wiki/Google')
page = BeautifulSoup(url.content, 'html.parser')
text = page.body.text

# Open file and write body of text
file = open('index.txt', 'w', encoding="utf-8")
file.write(text)
file.close()


# Tokenization with words and sentences
wtokens = nltk.word_tokenize(text)
stokens = nltk.sent_tokenize(text)

# Word tokenization
print('Word Tokenization: ')
for t in wtokens:
    print(t)

# Sentence tokenization
print('Sentence tokenization: ')
for s in stokens:
    print(s)

# POS tagging
print('Part Of Speech tagging: ')
posText = nltk.word_tokenize(text)
print(nltk.pos_tag(posText))

# Stemming
print('Porter Stemming: ')
pStemmer = PorterStemmer()
print(pStemmer.stem(text))

print('Lancaster Stemming: ')
lStemmer = LancasterStemmer()
print(lStemmer.stem(text))

print('Snowball Stemming: ')
sStemmer = SnowballStemmer('english')
print(sStemmer.stem(text))

# Lemmatization
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize(text))

# Trigram
print('Trigram: ')
wtokens = nltk.word_tokenize(text)
triword = trigrams(wtokens)
for g in triword:
    print(g)

# NER
print('Named Entity Recognition: ')
print(ne_chunk(pos_tag(wordpunct_tokenize(text))))
