# -*- coding: utf-8 -*-
"""Copy of Machine Learning - Linear Regression - Guided Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WPZDKEOtfNej8vfpf3BDDnIA3oOHtE6b

# Machine Learning - Linear Regression on Boston Housing Dataset

## Data Background and Problem Statement

We will take the Housing dataset which contains information about different houses in Boston. This data was originally a part of UCI Machine Learning Repository and has been removed now. We can also access this data from the scikit-learn library. There are 506 samples and 13 feature variables in this dataset. The objective is to predict the value of prices of the house using the given features.

# Task 1 : Environment Set up
"""

#import required libraries
import numpy as np
import pandas as pd

"""# Task 2 : Data Collection"""

# import the boston dataset
from sklearn.datasets import load_boston
boston_dataset = load_boston()

print(boston_dataset.DESCR)

# create a pandas dataframe and store the data
df_boston = pd.DataFrame(boston_dataset.data)
df_boston.columns = boston_dataset.feature_names

# append Price, target, as a new columnn to the dataset
df_boston['Price'] = boston_dataset.target

# print top 5 observations
df_boston.head()

df_boston.isnull().sum()

"""# Task 3 : Data Wrangling and EDA (Exploratory Data Analysis)"""

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.distplot(df_boston['Price'], bins=30)
plt.show()

"""#  Create a correlation matrix that measures the linear relationships between the variables"""

correlation_matrix = df_boston.corr().round(2)
# annot = True to print the values inside the square
sns.heatmap(data=correlation_matrix, annot=True)



"""# Write Your Observations

the largest amount is between 20 and 25

Theres a lot of outliers around 50

theres also alot around 10

# Preparing the data for training the Machine Learning Model
"""



# assign features on X axis 
X_features = boston_dataset.data

# assign target on Y axis 
Y_target = boston_dataset.target

"""# Build Linear Regression Model"""



# import linear model - the estimator
from sklearn.linear_model import LinearRegression
lineReg = LinearRegression()

# fit data into the the estimator
lineReg.fit(X_features,Y_target)

# print the intercept 
print('the estimated intercept %.2f '%lineReg.intercept_)

# print the coefficient 
print('the coefficient is %d ' %len(lineReg.coef_))

"""# Model Training"""

# train model split the whole dataset into train and test datasets
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X_features,Y_target)

# print the dataset shape
print(boston_dataset.data.shape)

# Print shapes of the training and testing data sets
print( X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)

# fit the training sets into the model
lineReg.fit(X_train,Y_train)

"""# Caluclate RMSE and R Square:

"""

from sklearn.metrics import mean_squared_error, r2_score

y_train_predict = lineReg.predict(X_train)

rmse = np.sqrt(mean_squared_error(Y_train,y_train_predict))

r2 = r2_score(Y_train, y_train_predict)
print("The model performance for training set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")

# model evaluation for testing set

y_test_predict = lineReg.predict(X_test)
# root mean square error of the model
rmse = (np.sqrt(mean_squared_error(Y_test, y_test_predict)))

# r-squared score of the model
r2 = r2_score(Y_test, y_test_predict)

print("The model performance for testing set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))

# plotting the y_test vs y_pred
# ideally should have been a straight line
plt.scatter(Y_test, y_test_predict)
plt.show()

"""# Your Conclusion

The predication for the y value looks to be correct when compairedd to the test

Most values with high density are around 20 to 25

Theres a fair amount of outliers
"""
