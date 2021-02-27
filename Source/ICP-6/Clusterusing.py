import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
import warnings

sns.set(style="white", color_codes=True)
warnings.filterwarnings("ignore")

# Read data set from file
dataset = pd.read_csv('CC.csv')

# Check if data set has null values
nullData = dataset.isnull().sum()
print(nullData)

# Replace null values with mean and check for null values again
dataset = dataset.fillna(dataset.mean())
nullData = dataset.isnull().sum()
print(nullData)

x = dataset.iloc[:, 1:]
y = dataset.iloc[:, -1]

# Use elbow method to know the number of clusters
wcss = []  # Within Cluster Sum of Squares

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, max_iter=300, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

# building the KMeans model
nclusters = 3  # Found from using the elbow method
km = KMeans(n_clusters=nclusters)
km.fit(x)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(x)

# Find and print the silhouette score
score = metrics.silhouette_score(x, y_cluster_kmeans)
print('Silhouette score: ' + str(score))
