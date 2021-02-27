import pandas as pd
from sklearn import metrics
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import preprocessing

# Read data set from file
dataset = pd.read_csv('CC.csv')
dataset = dataset.fillna(dataset.mean())

x = dataset.iloc[:, 1:]
y = dataset.iloc[:, -1]

# Feature scaling
scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns=x.columns)

# building the KMeans model on the scaled features
nclusters = 3
km = KMeans(n_clusters=nclusters)
km.fit(X_scaled)
y_cluster_kmeans = km.predict(X_scaled)

# Find and print the silhouette score
score = metrics.silhouette_score(X_scaled, y_cluster_kmeans)
print('Silhouette score with scaling: ' + str(score))
