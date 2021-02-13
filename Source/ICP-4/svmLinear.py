import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC

# Read file and do data training and testing
df = pd.read_csv('glass.csv')
x = df.drop("Type",axis=1)
y = df["Type"]
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# Linear SVC algorithm
svc = LinearSVC()
svc.fit(X_train, Y_train)
y_pred = svc.predict(X_test)
svc_score = round(svc.score(X_train, Y_train) * 100, 2)

# Print accuracy score
print("Linear SVM accuracy is:", svc_score)
# Print the classification report
print('Classification report: \n' + classification_report(Y_test, y_pred))

