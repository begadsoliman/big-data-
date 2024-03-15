from sklearn.cluster import KMeans
import pandas as pd

# Load the dataset
df = pd.read_csv('/home/doc-bd-a1/service-result/res_dpre.csv')

from sklearn.decomposition import PCA
pca = PCA(n_components=2)  # Choose the number of components based on your needs

pca_result = pca.fit_transform(df)

kmeans = KMeans(n_clusters=3, n_init=10)
kmeans.fit(pca_result)

cluster_counts = pd.Series(kmeans.labels_).value_counts().to_frame(name='Count')
cluster_counts.to_csv('/home/doc-bd-a1/service-result/k.txt', index=False)
