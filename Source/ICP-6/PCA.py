import pandas as pd
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
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

# PCA on data set
pca = PCA(2)
x_pca = pca.fit_transform(X_scaled)

# KMean on PCA
nclusters = 3
km = KMeans(n_clusters=nclusters)
km.fit(X_scaled)
y_cluster_kmeans = km.predict(X_scaled)

# Print silhouette score
score = metrics.silhouette_score(x_pca, y_cluster_kmeans)
print('Silhouette score with PCA: ' + str(score))

# Visualize the plot
plt.scatter(x_pca[:, 0], x_pca[:, 1], c=y_cluster_kmeans)
plt.show()



