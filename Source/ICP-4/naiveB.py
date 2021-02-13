import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Read file and do data training and testing
df = pd.read_csv('glass.csv')
x = df.drop("Type",axis=1)
y = df["Type"]
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# Naive Bayes algorithm
nb = GaussianNB()
nb.fit(X_train, Y_train)
y_pred = nb.predict(X_test)
nb_score = round(nb.score(X_train, Y_train) * 100, 2)

# Print accuracy score
print("Naive Bayes accuracy is:", nb_score)
# Print the classification report
print('Classification report: \n' + classification_report(Y_test, y_pred))

