import pandas as pd
from sklearn.preprocessing import StandardScaler

scle = StandardScaler()

df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')

import statsmodels.api as sm

df['Model_ord'] = pd.Categorical(df.Model).codes
X = df[['Mileage', 'Cylinder', 'Doors']]
y = df[['Price']]
X[['Mileage','Cylinder','Doors']]=scle.fit_transform(X[['Mileage','Cylinder','Doors']].as_matrix())
#X1 = sm.add_constant(X)
est = sm.OLS(y, X).fit()

est.summary()

