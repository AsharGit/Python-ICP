from keras.layers import Input, Dense
from keras.models import Model
from matplotlib import pyplot as plt

# this is the size of our encoded representations
encoding_dim = 32  # 32 floats -> compression of factor 24.5, assuming the input is 784 floats

# this is our input placeholder
input_img = Input(shape=(784,))
# "encoded" is the encoded representation of the input
encoded = Dense(encoding_dim, activation='relu')(input_img)
# Add a new hidden layer for encoding
hiddenLayer1 = Dense(encoding_dim, activation='relu')(encoded)
# Add a new hidden layer for decoding
hiddenLayer2 = Dense(encoding_dim, activation='relu')(hiddenLayer1)
# "decoded" is the lossy reconstruction of the input
decoded = Dense(784, activation='sigmoid')(hiddenLayer2)
# this model maps an input to its reconstruction
autoencoder = Model(input_img, decoded)
# this model maps an input to its encoded representation
autoencoder.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
from keras.datasets import mnist, fashion_mnist
import numpy as np

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

history = autoencoder.fit(x_train, x_train,
                          epochs=5,
                          batch_size=256,
                          shuffle=True,
                          validation_data=(x_test, x_test))

# Prediction model on x_test
prediction = autoencoder.predict(x_test)
# Plot the first image in the x_test data set
plt.imshow(x_test[0].reshape(28, 28), cmap='gray')
plt.show()

# Show the compressed middle layer between encoding and decoding
compress = Model(input_img, encoded)
comp = compress.predict(x_test[0].reshape(1, 784))
plt.imshow(comp.reshape(16, 2), cmap='gray')
plt.show()

# Plot the same reconstructed image
plt.imshow(prediction[0].reshape(28, 28), cmap='gray')
plt.show()

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
