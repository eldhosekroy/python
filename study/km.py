import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()
x = iris.data

kmeans = KMeans(n_clusters = 3, random_state =42)
kmeans.fit(x)
cl = kmeans.labels_

plt.subplot(1,2,1)

plt.scatter(x[:,0],x[:,1], c = cl, cmap='turbo')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],marker='x', s = 200, label='Centroid')

plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.title('Iris Data Kmeans')
plt.legend()
plt.show()
