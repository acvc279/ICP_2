import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.core import Dense
#load data
df = pd.read_csv('Breas Cancer.csv')
#convert
c = {"diagnosis": {"M": 0, "B": 1}}
cancer_data = df.replace(c)
x = cancer_data.iloc[:,2:31]
y = cancer_data['diagnosis']
#train test split
X_train, X_test, Y_train, Y_test = train_test_split(x, y,test_size=0.25, random_state=87)
#Sequential
np.random.seed(155)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(20, input_dim=29, activation='relu')) # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
#compilation
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,initial_epoch=0)
#Summary with Accuracy
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test))

#second defence layer
#Sequential
np.random.seed(155)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(20, input_dim=29, activation='relu')) # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
#compilation
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,initial_epoch=0)
#Summary with Accuracy
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test))