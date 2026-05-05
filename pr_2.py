import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error, silhouette_score
# Load built-in Iris dataset
iris = load_iris()
X = iris.data  # features
# Convert to DataFrame (optional but useful)
df = pd.DataFrame(X, columns=iris.feature_names)
# -------------------------------
# K-Means Clustering
# -------------------------------
kmean = KMeans(n_clusters=3, random_state=42)
kmean.fit(X)
# Predict cluster labels
cluster_numbers = kmean.predict(X)
# -------------------------------
# Elbow Method
# -------------------------------
WCSS = []
for i in range(1, 11):
    kmean_temp = KMeans(n_clusters=i, random_state=42)
    kmean_temp.fit(X)
    WCSS.append(kmean_temp.inertia_)
# Plot Elbow Graph
plt.figure()
plt.plot(range(1, 11), WCSS, marker='x')
plt.title('The Elbow Method Graph')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()
# -------------------------------
# Scatter Plot (First 2 features)
# -------------------------------
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=cluster_numbers, cmap='rainbow')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('K-Means Clustering on Iris Dataset')
plt.show()
# -------------------------------
# Evaluation Metrics
# -------------------------------
mse = mean_squared_error(X, kmean.cluster_centers_[cluster_numbers])
sil_score = silhouette_score(X, cluster_numbers)
print("MSE:", mse)
print("Silhouette Score:", sil_score)