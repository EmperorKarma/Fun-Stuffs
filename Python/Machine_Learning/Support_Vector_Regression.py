'''Importing Libraries'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''Importing The Dataset'''
Data_set = pd.read_csv('E:\Machine Learning Resources\Machine Learning A-Z (Codes and Datasets)\Part 2 - Regression\Section 7 - Support Vector Regression (SVR)\Python\Position_Salaries.csv')
X = Data_set.iloc[:, 1:-1].values
Y = Data_set.iloc[:, -1].values

Y = Y.reshape(len(Y) , 1)

'''Feature Scaling'''
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_Y = StandardScaler()
X = sc_X.fit_transform(X)
Y = sc_Y.fit_transform(Y)

'''Training The SVR On The Whole Dataset'''
from sklearn.svm import SVR
Regressor = SVR(kernel = 'rbf')
Regressor.fit(X,Y.ravel())

'''Predicting A New Result'''
P = sc_Y.inverse_transform(Regressor.predict(sc_X.transform([[6.5]])).reshape(1,-1))
print(P)

'''Visualizing The Support Vector Regression'''
plt.scatter(sc_X.inverse_transform(X), sc_Y.inverse_transform(Y).reshape(1,-1), color = 'red')
plt.plot(sc_X.inverse_transform(X), sc_Y.inverse_transform(Regressor.predict(X).reshape(-1,1)), color = 'blue')
plt.title('Truth or Bluff (Support Vector Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

'''Visualizing The Support vector Regression'''
X_grid = np.arange(min(sc_X.inverse_transform(X)), max(sc_X.inverse_transform(X)), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(sc_X.inverse_transform(X), sc_Y.inverse_transform(Y), color = 'red')
plt.plot(X_grid, sc_Y.inverse_transform(Regressor.predict(sc_X.transform(X_grid)).reshape(-1,1)), color = 'blue')
plt.title('Truth or Bluff (Support Vector Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()