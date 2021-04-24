from keras.models import load_model
from keras_preprocessing.sequence import pad_sequences
from sentimentAnalysis import tokenizer

# Load the model
model = load_model("sentiment.h5")

sentence = ["A lot of good things are happening. We are respected again throughout the world, "
            "and that's a great thing."]  # @realDonaldTrump

# Tokenize the sentence into a sequence of integers
tokenizer.fit_on_texts(sentence)
sentence = tokenizer.texts_to_sequences(sentence)
# Pad the sequence
sentence = pad_sequences(sentence, maxlen=28)
# Make the prediction on the sequence
result = model.predict(sentence)
# Print the result
print(result)




