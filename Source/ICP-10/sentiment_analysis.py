from keras.models import Sequential
from keras import layers
from keras.preprocessing.text import Tokenizer
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.layers.embeddings import Embedding
from keras.layers import Flatten
from keras.preprocessing.sequence import pad_sequences
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_20newsgroups

#df = pd.read_csv('imdb_master.csv',encoding='latin-1')
#print(df.head())
# sentences = df['review'].values
# y = df['label'].values
df = fetch_20newsgroups(subset='train', shuffle=True)
sentences = df.data
y = df.target


#tokenizing data
tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(sentences)

# Prepare data for embedding layers
max_review_len = max([len(s.split()) for s in sentences])
vocab_size = len(tokenizer.word_index)+1
sentences = tokenizer.texts_to_sequences(sentences)
padded_docs = pad_sequences(sentences,maxlen=max_review_len)

#getting the vocabulary of data
#sentences = tokenizer.texts_to_matrix(sentences)

le = preprocessing.LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(padded_docs, y, test_size=0.25, random_state=1000)

# Number of features
input_dim = 2000

model = Sequential()
model.add(Embedding(vocab_size, 50, input_length=max_review_len))
model.add(Flatten())
# Mistake 1: input dim used without being given a value
model.add(layers.Dense(300,input_dim=input_dim, activation='relu'))
# Mistake 2: We only have an input layer and output layer
# we need a dense layer in the middle to complete a neural network
model.add(layers.Dense(100, activation='sigmoid'))
# Mistake 3: the activation function is sigmoid which produces output between 0 and 1
# We are splitting output into 3 categories (pos, neg, unsup) so softmax should be used
model.add(layers.Dense(3, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['acc'])
history=model.fit(X_train,y_train, epochs=5, verbose=True, validation_data=(X_test,y_test), batch_size=256)

# Model Accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Training', 'Testing'], loc='best')
plt.show()

# Model Loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Training', 'Testing'], loc='best')
plt.show()
