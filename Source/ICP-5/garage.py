import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

train = pd.read_csv('data.csv')
##handling missing value
data = train.select_dtypes(include=[np.number]).interpolate().dropna()
y = data['SalePrice']
X = data['GarageArea']

# Visualize the scatter plot of Garage Area Vs. Sale Price
plt.scatter(X, y, alpha=.75, color='b')
plt.title("Garage Area Vs. Sale Price")
plt.xlabel('GarageArea')
plt.ylabel('SalePrice')
plt.show()


print(X.describe())
print(stats.zscore(X))


