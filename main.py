import warnings
import pandas as pd
from figure import plot
from sklearn.model_selection import train_test_split

from datasets import T1_obr
from analysis.models import *

warnings.filterwarnings('ignore')

start = pd.to_datetime('2020-01-01')
stop = pd.to_datetime('2020-01-02')
cols = ['TS_T1_obr', ]

# load data
df = T1_obr()

# prep data
plot(df, colsi=cols, start=str(start), stop=str(stop))
df1 = df[['TS_T1_obr','TS_T1_prm']]
df1.index = df1.index.tz_localize(None)
filter1 = ['2020-05-31','2020-06-16']
filter2 = ['2021-05-15','2021-05-31']
filter3 = ['2022-08-14','2022-08-31']
_filter = (((df1.index>pd.to_datetime(filter1[0])) & (df1.index<pd.to_datetime(filter1[1]))) |\
    ((df1.index>pd.to_datetime(filter2[0])) & (df1.index<pd.to_datetime(filter2[1]))) |\
    ((df1.index>pd.to_datetime(filter3[0])) & (df1.index<pd.to_datetime(filter3[1]))))
df1[_filter] = None

# Преобразую данные для прогноза
for i in [4,5,6,23,24]:
    df1[f'T1_obr_{i}'] = df1['TS_T1_obr'].shift(i)
    df1[f'T1_prm_{i}'] = df1['TS_T1_prm'].shift(i)
df1 = df1.drop(columns = ['TS_T1_prm'])
df1 = df1.dropna()

# train-test-split
xtrain,xtest, ytrain,ytest = train_test_split(df1.iloc[:,1:], df1.iloc[:,[0]], test_size=0.2, shuffle=False)

forecast_df1 = catboost_forecast(xtrain, ytrain, xtest, ytest)
forecast_df2 = LGBM_forecast(xtrain, ytrain, xtest, ytest)
forecast_df3 = LinearRegression_forecast(xtrain, ytrain, xtest, ytest)
forecast_df4 = Ridge_forecast(xtrain, ytrain, xtest, ytest)

import matplotlib.pyplot as plt

plot(forecast_df1, ['TS_T1_obr','predict'], '2022-10-28', '2022-11-04', 'catboost_forecast')
plot(forecast_df2, ['TS_T1_obr','predict'], '2022-10-28', '2022-11-04', 'LGBM_forecast')
plot(forecast_df3, ['TS_T1_obr','predict'], '2022-10-28', '2022-11-04', 'LinearRegression_forecast')
plot(forecast_df4, ['TS_T1_obr','predict'], '2022-10-28', '2022-11-04', 'Ridge_forecast')
plt.show()