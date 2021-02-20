import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

#read the data from rev.csv
d = pd.read_csv('rev.csv')

#String to integer convertion
c = {"City Group": {"Big Cities": 0, "Other": 1}, "Type": {"FC": 0, "IL": 1, "DT": 2}}
data = d.replace(c)

#Split train and test the data
x = data.drop(['revenue', 'Id'], axis=1)
y = np.log(data.revenue)
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=10, test_size=0.25)

#Linear regression model
reg = linear_model.LinearRegression()
model = reg.fit(x_train, y_train)

#Evaluating the model using RMSE and R2 score
print("\nR2 : ", model.score(x_test, y_test))
pred = model.predict(x_test)
print("\nRMSE : ", mean_squared_error(y_test, pred))

#Mathplot visualization for predictions and tests
plt.scatter(pred, y_test, color='k', alpha=1)
plt.grid(b=True, which='both', color='grey', linestyle='--')
plt.xlabel("Predicted Price")
plt.ylabel("Actual Price")
plt.title("Linear Regression")
plt.show()

#Top 5 correlated features finding
n = data.select_dtypes(include=[np.number])
cr = n.corr()
print('\n', cr['revenue'].sort_values(ascending=False)[:6], '\n')
print(cr['revenue'].sort_values(ascending=False)[-6:])

#Again Split train test for top 5 features
x2 = data[['P2', 'P28', 'P6', 'P21', 'P11']]
y2 = np.log(data.revenue)
x_train2, x_test2, y_train2, y_test2 = train_test_split(x2, y2, random_state=10, test_size=0.25)

#Linear regression model for top features
reg1 = linear_model.LinearRegression()
model1 = reg1.fit(x_train2, y_train2)

#Evaluating the model using RMSE and R2 score
print("\nR2 for top 5 corr features : ", model1.score(x_test2, y_test2))
pred1 = model1.predict(x_test2)
print("\nRMSE for top 5 corr features : ", mean_squared_error(y_test2, pred1))

#Plot for top features
plt.scatter(pred1, y_test2, color='r', alpha=1)
plt.grid(b=True, which='both', color='k', linestyle='--')
plt.xlabel("Predicted Price")
plt.ylabel("Actual Price")
plt.title("Linear Regression")
plt.show()
