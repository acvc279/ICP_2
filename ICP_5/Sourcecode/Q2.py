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
