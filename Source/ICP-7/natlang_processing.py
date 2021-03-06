import requests
from bs4 import BeautifulSoup
import nltk
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk import trigrams
from nltk import wordpunct_tokenize, ne_chunk, pos_tag


url = requests.get('https://en.wikipedia.org/wiki/Google')
page = BeautifulSoup(url.content, 'html.parser')


file = open('index.txt', 'w', encoding="utf-8")
file.write(page.body.text)
file.close()

text = page.body.text

# # Tokenization with words and sentences
# wtokens = nltk.word_tokenize(text)
# stokens = nltk.sent_tokenize(text)
#
# # Word tokenization
# for t in wtokens:
#     print(t)
# # Sentence tokenization
# for s in stokens:
#     print(s)

# # POS tagging
# posText = nltk.word_tokenize(text)
# print(nltk.pos_tag(posText))
#
# # Stemming
# print('Porter Stemming: ')
# pStemmer = PorterStemmer()
# print(pStemmer.stem(text))
#
# print('Lancaster Stemming: ')
# lStemmer = LancasterStemmer()
# print(lStemmer.stem(text))
#
# print('Snowball Stemming: ')
# sStemmer = SnowballStemmer('english')
# print(sStemmer.stem(text))

# Lemmatization
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize(text))

# Trigram
wtokens = nltk.word_tokenize(text)
triword = trigrams(wtokens)
for g in triword:
    print(g)

# NER
print(ne_chunk(pos_tag(wordpunct_tokenize(text))))
