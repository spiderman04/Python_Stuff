# Simple ML model from You Tube Tutorial

"""Another copy of first-proj-model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PEUOEa7Lwqq1J1Vx

First project Model

# My Simple Python Data Model
https://www.youtube.com/playlist?list=PLtqF5YXg7GLn0WWB_wQx7wHrIvbs0EH2e

# Load Data

## Splitting Data
"""

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')

from sklearn.model_selection import train_test_split

y = df['logS']
x = df.drop('logS', axis=1)

# the Training Set will be 80% and Testing Set at 20%
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.2, random_state=100)

x_train

x_test

y_train

"""## Model Building

"""



"""## Linear Regression"""

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train, y_train)

"""###Applying the model to make a prediction"""

y_lr_train_pred = lr.predict(x_train)
y_lr_test_pred = lr.predict(x_test)

print(y_lr_train_pred)  # 80% of data

"""###Evaluate model performance

"""

from sklearn.metrics import mean_squared_error, r2_score

lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)
lr_train_r2 = r2_score(y_train, y_lr_train_pred)

lr_test_mae = mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2 = r2_score(y_test, y_lr_test_pred)

print('LR MAE Train: ', lr_train_mse, lr_test_mae)

print('LR R2 Train: ',lr_train_r2, lr_test_r2)

lr_results = pd.DataFrame(['Linear Regression', lr_train_mse, lr_train_r2, lr_test_mae, lr_test_r2]).transpose()
lr_results.columns = ['Method', 'Training MAE', 'Training R2', 'Test MAE', 'Test R2']

lr_results

"""#Random Forest

Data visualization of prediction results
"""

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(5,5))
plt.scatter(x=y_train, y=y_lr_train_pred, c="#7CAE00", alpha=0.3)

z = np.polyfit(y_train, y_lr_train_pred, 1)
p = np.poly1d(z)

plt.plot(y_train, p(y_train), '#F8766D')
plt.ylabel('Predict Logs')
plt.xlabel('Experimental LogS')
