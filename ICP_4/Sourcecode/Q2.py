import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
data = pd.read_csv("glass.csv")
x = data.iloc[:, 0:9]
y = data.iloc[:, -1]
x = x.values
y = y.values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
classifier = GaussianNB()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
a = accuracy_score(y_test, y_pred)
print("Accuracy = ", a)
