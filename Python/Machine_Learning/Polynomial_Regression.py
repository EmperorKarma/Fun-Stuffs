'''Importing The Libraires'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


'''Importing The DataSets'''
data_set = pd.read_csv('E:\Machine Learning Resources\Machine Learning A-Z (Codes and Datasets)\Part 2 - Regression\Section 6 - Polynomial Regression\Python\Position_Salaries.csv')
X = data_set.iloc[:,1 :-1].values
Y = data_set.iloc[:, -1].values

'''Traning The Linear Regresssion Model On The Whole Dataset'''
from sklearn.linear_model import LinearRegression
Lin_reg = LinearRegression()
Lin_reg.fit(X, Y)

'''Traning The Polynomial Regression On The Whole Dataset'''
from sklearn.preprocessing import PolynomialFeatures
Poly_reg = PolynomialFeatures(degree = 4)
X_Poly = Poly_reg.fit_transform(X)
Poly_reg_2 = LinearRegression()
Poly_reg_2.fit(X_Poly , Y)

'''Visualizing The Linear Regression
plt.scatter(X , Y , color = 'red')
plt.plot(X , Lin_reg.predict(X) ,  color = 'blue')
plt.title("Truth Or Bluff (Linear Regression)")
plt.xlabel('Position Level')
plt.ylabel("Salary")
plt.show()'''

'''Visualizing The Polynomial Regression
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()'''




'''Visuallizing The Polynomial Regression In Smooth Curve
X_Grid = np.arange(min(X), max(X) ,0.1)
X_Grid = X_Grid.reshape(len(X_Grid),1)
plt.scatter(X , Y , color = 'red')
plt.plot(X_Grid , Poly_reg_2.predict( Poly_reg.fit_transform(X_Grid)) ,  color = 'blue')
plt.title("Truth Or Bluff (Polynomial Regression)")
plt.xlabel('Position Level')
plt.ylabel("Salary")
plt.show()'''

'''Predecting a New Results In Linear Regression'''
#Predict_Lin = Lin_reg.predict([[6.5]])
#print(Predict_Lin)

'''Predecting a New Results In Polynomial Regression'''
Predict_Poly = Poly_reg_2.predict(Poly_reg.fit_transform([[6.5]]))
print(Predict_Poly)