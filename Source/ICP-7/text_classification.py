from sklearn.datasets import fetch_20newsgroups

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

tfidf_Vect = TfidfVectorizer()
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)

# Using NB classifier
clf = MultinomialNB()  # Accuracy: 0.7738980350504514
clf.fit(X_train_tfidf, twenty_train.target)

# Testing
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
predicted = clf.predict(X_test_tfidf)

# Scoring
score = metrics.accuracy_score(twenty_test.target, predicted)
print('Multinomial NB classifer score: ' + str(score))

# Using SVM classifier
clf = SVC()  # Accuracy: 0.8186404673393521
clf.fit(X_train_tfidf, twenty_train.target)

# Testing
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
predicted = clf.predict(X_test_tfidf)

# Scoring
score = metrics.accuracy_score(twenty_test.target, predicted)
print('SVM classifer score: ' + str(score))

# Using bigram
tfidf_Vect = TfidfVectorizer(ngram_range=(1, 2))
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)

# Using SVM classifier
clf = SVC()  # Accuracy: 0.8043016463090813
clf.fit(X_train_tfidf, twenty_train.target)

# Testing
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
predicted = clf.predict(X_test_tfidf)

# Scoring
score = metrics.accuracy_score(twenty_test.target, predicted)
print('SVM classifer score with bigram: ' + str(score))

# Using stop words
tfidf_Vect = TfidfVectorizer(stop_words='english')
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)

# Using SVM classifier
clf = SVC()  # Accuracy: 0.8252788104089219
clf.fit(X_train_tfidf, twenty_train.target)

# Testing
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
predicted = clf.predict(X_test_tfidf)

# Scoring
score = metrics.accuracy_score(twenty_test.target, predicted)
print('SVM classifer score with stop words: ' + str(score))

