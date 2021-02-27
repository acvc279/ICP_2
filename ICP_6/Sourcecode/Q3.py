import pandas as pd
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")
#Data imported
Data = pd.read_csv('CC.csv')
#Find the NULL values
print('\nFinding Null Values', Data.isnull().sum())
#replaceing mean values
Data['MINIMUM_PAYMENTS'].fillna(value = Data['MINIMUM_PAYMENTS'].mean(), inplace = True)
Data['CREDIT_LIMIT'].fillna(value=Data['CREDIT_LIMIT'].mean(), inplace=True)
#checking again for conformation whether null values were replaced or not
print("\nAfter replacing null values to mean:\n", Data.isnull().sum())
#split the data
x = Data.iloc[:, 1:]
print('\nX Shape : ', x.shape)
y = Data.iloc[:, -1]
print('Y shape : ', y.shape)
#implementing elbow model
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
#plot
plt.plot(range(1, 11), wcss)
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('Elbow model')
plt.show()
#from the graph we take kmeans
nclusters = 3
km = KMeans(n_clusters=nclusters)
km.fit(x)
#predicting cluaster
y_cluster_kmeans = km.predict(x)
score = metrics.silhouette_score(x, y_cluster_kmeans)
print('Silhouette score when k = 3 is :',score)
# Applying PCA
scler = StandardScaler() #Applying scaling
scler.fit(x)
# Apply transform to both the training set and the test set.
x_scler = scler.transform(x)
pca = PCA(2)
x_pca = pca.fit_transform(x_scler)
ndata = pd.DataFrame(data=x_pca)
#elbow method to know the number of clusters
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x_pca)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()
# Appling Kmeans over PCA scaled features
nclusters = 4 # this is the k in kmeans from above graph
km = KMeans(n_clusters=nclusters)
km.fit(x_pca)
#Silhouette score
y_cluster_kmeans = km.predict(x_pca)
scre = metrics.silhouette_score(x_pca, y_cluster_kmeans)
print('Silhouette score after scaling when k = 4 is :',scre)