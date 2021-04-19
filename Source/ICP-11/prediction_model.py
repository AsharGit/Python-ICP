import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.constraints import maxnorm
from keras.optimizers import SGD
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras.models import load_model
from keras import backend as K
K.set_image_data_format('channels_first')

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load data
data = load_model("layermodel.h5")
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

category = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog",
            "horse", "ship", "truck"]

prediction = data.predict([X_test])

# Loop to show the real
for i in range(4):
    print("Using test sample image " + str(i))
    plt.imshow(X_test[i].reshape(32, 32, 3))
    plt.show()
    print("Real category: " + category[np.argmax(prediction[i])])
    print("Predicted category: " + category[y_test[i][0]] + "\n")

