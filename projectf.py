# -*- coding: utf-8 -*-
"""projectf.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19-YEBtDrMSkYscw5-28QDhieZqWSDRzS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler

data=pd.read_csv("/content/Avocado2.csv")

data.head()

data.isnull().sum()

x=data.drop(['AveragePrice'] ,axis=1)
y=data['AveragePrice']

print(x)

print(y)




x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=True)

lin_reg_model=LinearRegression()

reg=lin_reg_model.fit(x_train,y_train)

w=reg.score(x_test,y_test)

reg.score(x_train,y_train)

train_prediction=lin_reg_model.predict(x_train)

error_score=metrics.r2_score(y_train,train_prediction)
print(error_score)



from sklearn import linear_model
lasso_reg=linear_model.Lasso(alpha=50,max_iter=100,tol=0.1)
lasso_reg.fit(x_train,y_train)

j=lasso_reg.score(x_test,y_test)
trainl_prediction=lasso_reg.predict(x_train)
error2_score=metrics.r2_score(y_train,trainl_prediction)
print(error2_score)

jj=lasso_reg.score(x_train,y_train)

from sklearn.linear_model import Ridge
Ridge_reg=linear_model.Ridge(alpha=50,max_iter=100,tol=0.1)
Ridge_reg.fit(x_train,y_train)
trainr_prediction=Ridge_reg.predict(x_train)
error_scorer=metrics.r2_score(y_train,trainr_prediction)
print(error_scorer)
ff=Ridge_reg.score(x_train,y_train)

ll=Ridge_reg.score(x_test,y_test)