'''Importing The Libraires'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''Importing The DataSets'''
data_set = pd.read_csv('E:/Machine Learning Resources/Machine Learning A-Z (Codes and Datasets)/Part 1 - Data Preprocessing/Section 2 -------------------- Part 1 - Data Preprocessing --------------------/Python/Data.csv')
X = data_set.iloc[:, :-1].values
Y = data_set.iloc[:, -1].values
print(X)
print(Y)

'''Taking Care Of Missing Data'''
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan , strategy = 'mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X)

'''Encoding The Independent Varible'''
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers = [ ('encoder', OneHotEncoder(), [0]) ], remainder = 'passthrough')
X = np.array(ct.fit_transform(X))
print(X)

'''Encoding The Dependent Variable'''
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
Y = le.fit_transform(Y)
print(Y)

'''Splitting The Dataset into The Training Set And Test Set'''
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size = 0.2 , random_state = 1)
print(X_train)
print(X_test)
print(Y_train)
print(Y_test)

'''Feature Scaling'''
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])
print(X_train)
print('\n')
print(X_test)
