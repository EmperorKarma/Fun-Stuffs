'''Importing The Libraries'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''Importing The Dataset'''
Data_set = pd.read_csv('E:\Machine Learning Resources\Machine Learning A-Z (Codes and Datasets)\Part 2 - Regression\Section 4 - Simple Linear Regression\Python\Salary_Data.csv')
X = Data_set.iloc[:, :-1].values
Y = Data_set.iloc[:, -1].values

'''Importing The Dataset into Training Set And Test Set'''
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size = 0.2 , random_state = 0)

'''Training The Simpler Linear Regression Model On The Training Set'''
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train , Y_train)

'''Predicting The Test Set Results'''
Y_pred = regressor.predict(X_test)

'''Visualising The Training Set Results'''
plt.scatter(X_train , Y_train , color = 'red')
plt.plot(X_train , regressor.predict(X_train) , color = 'blue')
plt.title('Salary Vs Experience Relationship Graph (Training Set)')
plt.xlabel('Years Of The Experince')
plt.ylabel('Salary')
plt.show()

'''Visualising The Test SET Results'''
plt.scatter(X_test , Y_test , color = 'red')
plt.plot(X_train , regressor.predict(X_train) , color = 'blue')
plt.title('Salary Vs Experience Relationship Graph (Test Set)')
plt.xlabel('Years Of The Experince')
plt.ylabel('Salary')
plt.show()

'''Making The Single Predections'''
print(regressor.predict([[12]]))

'''Getting The Final Linear Regression Equation With The Values Of The Coefficients'''
#print(regressor.coef_)
#print(regressor.intercept_)