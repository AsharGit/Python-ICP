from keras.models import Sequential
from keras.layers.core import Dense, Activation

# load dataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

sc = StandardScaler()
# Read file
dataset = pd.read_csv("breastcancer.csv")

x = dataset.iloc[:, 2:31]
x_scaled = sc.fit_transform(x)  # Normalized data
y = dataset['diagnosis'].map({'M': 1, 'B': 0}).astype(int)  # Map categorical data to int

# Train data
# X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.25, random_state=87)
X_train, X_test, Y_train, Y_test = train_test_split(x_scaled, y, test_size=0.25, random_state=87)

# Create a neural network
np.random.seed(155)
my_first_nn = Sequential()  # create model
my_first_nn.add(Dense(50, input_dim=29, activation='relu'))  # hidden layer
my_first_nn.add(Dense(20, activation='relu'))  # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid'))  # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,
                                     initial_epoch=0)
# Print accuracy score
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test))
