'''Importing The Libraries'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''Importing The Dataset'''
Data_set = pd.read_csv('E:\Machine Learning Resources\Machine Learning A-Z (Codes and Datasets)\Part 2 - Regression\Section 5 - Multiple Linear Regression\Python\Startups.csv')
X = Data_set.iloc[:, :-1].values
Y = Data_set.iloc[:, -1].values



'''Encoding The Categorical Data'''
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers = [ ('encoder', OneHotEncoder(), [3]) ], remainder = 'passthrough')
X = np.array(ct.fit_transform(X))

'''Importing The Dataset into Training Set And Test Set'''
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size = 0.2 , random_state = 0)


'''Training the Multiple Linear Regression on The Dataset'''
from sklearn.linear_model import LinearRegression
regresssor = LinearRegression()
regresssor.fit(X_train , Y_train)


'''Predecting The Test set'''
Y_pred = regresssor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((Y_pred.reshape(len(Y_pred),1),Y_test.reshape(len(Y_test),1) ),1))
