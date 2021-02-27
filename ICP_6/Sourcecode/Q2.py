#Importing libraries
import pandas as pd
from sklearn import metrics
from sklearn import preprocessing
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")
# Feauture Scaling
Data = pd.read_csv('CC.csv')
#Find the NULL values
print('\nFinding Null Values', Data.isnull().sum())
#replaceing mean values
Data['MINIMUM_PAYMENTS'].fillna(value=Data['MINIMUM_PAYMENTS'].mean(), inplace=True)
Data['CREDIT_LIMIT'].fillna(value=Data['CREDIT_LIMIT'].mean(), inplace=True)
#checking again for conformation whether null values were replaced or not
print("\nAfter replacing null values to mean:\n", Data.isnull().sum())
#split the data
x = Data.iloc[:, 1:]
print('\nX Shape : ', x.shape)
y = Data.iloc[:, -1]
print('Y shape : ', y.shape)
#feature scaling
scler = preprocessing.StandardScaler()
scler.fit(x)
X_scled_array = scler.transform(x)
X_scled = pd.DataFrame(X_scled_array, columns=x.columns)
#Elbow model
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X_scled)
    wcss.append(kmeans.inertia_)
#plot
plt.plot(range(1, 11), wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss after scaling')
plt.show()
#After scaled features here applied kmeans
nclusters = 4
km = KMeans(n_clusters=nclusters)
km.fit(X_scaled)
#Silhouette score
y_cluster_kmeans = km.predict(X_scled)
scre = metrics.silhouette_score(X_scled, y_cluster_kmeans)
print('After scaling theSilhouette score k = 4 is :', scre)
