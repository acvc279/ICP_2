#imported libraries
import pandas as pd
from sklearn import metrics
from sklearn.cluster import KMeans
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
plt.plot(range(1, 10), wcss)
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('Elbow model')
plt.show()
#finding Silhouette score
#From the above graph we take kmeans in a nclusters
nclusters = 3
km = KMeans(n_clusters=nclusters)
km.fit(x)
# predicting cluaster
y_cluster_kmeans = km.predict(x)
score = metrics.silhouette_score(x, y_cluster_kmeans)
print('Silhouette score when k = 3 is :',score)