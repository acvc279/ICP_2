import pandas as pd
import matplotlib.pyplot as plt

#Read the data from data.csv file
data = pd.read_csv("data.csv")

#finding complete statical details of the data
print(data.GarageArea.describe())

#Centered values
outlier = data[(data.GarageArea > 334) & (data.GarageArea < 576)]

#plot before removing outliers
plt.scatter(data.GarageArea, data.SalePrice, color='k', alpha=0.75)

#After removing the anomalies from the data for plot
plt.scatter(outlier.GarageArea, outlier.SalePrice, color='darkviolet', alpha=0.5)
plt.grid(b=True, which='both', color='grey', linestyle='--')
plt.xlabel("GarageArea")
plt.ylabel("SalePrice")
plt.title("")
plt.show()
