# -*- coding: utf-8 -*-
"""movingAverage.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DP0ZeRU58lRXNwcC4-5RFxlVy3pBim4l
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
from google.colab import drive
drive.mount('/content/drive')
df = pd.read_csv('/content/drive/MyDrive/UCI Conference/Dataset2/ocCovidCount.csv', index_col='date', parse_dates=True)
#df = pd.read_csv('/content/drive/MyDrive/UCI Conference/ocCovidCountDataset/ocCovidCount.csv')
#df["date"] = pd.to_datetime(df["date"])
df.sort_values(by='date', ascending = True, inplace = True)
N = 3186989
df['Infective'] = df['Infective'].div(N)
df.head(60)

df['Infective'].plot(figsize=(30,10))
df['Infective'].rolling(window=7).mean().plot(figsize=(30,10))
df['Infective'].rolling(window=28).mean().plot(figsize=(30,10))

df['7-day Avg'] = df['Infective'].rolling(window=7).mean()
df['28-day Avg'] = df['Infective'].rolling(window=28).mean()


#df['Infective'].plot()
#df['7-day Avg'].plot(figsize=(30,10)).legend()
#df['28-day Avg'].plot(figsize=(30,10)).legend()

fig1 = plt.figure(1); fig1.clf()
plt.plot(df['Infective'], label='Daily Cases')
plt.plot(df['7-day Avg'], label='7-day Moving Average')
plt.plot(df['28-day Avg'], label='28-day Moving Average')
fig1.legend(loc='center right')
plt.title('Figure 1: Orange County COVID-19 Cases')
plt.ylabel('Population')
plt.xlabel('Date')
plt.figure(figsize=(10,10))

# # def moving_average(period, data):
#   size = len(data)n_groups = (size - period) + 1
#   retList = [0] * n_groups
#   start = 0
#   sum = 0

#   for i in range(n_groups):
#     for j in range(period):
#       sum += data[start + j]
#     retList[i] = sum/period
#     sum = 0
#     start += 1

#   lagList = [0] * (period - 1)
#   retList = lagList + retList

#   return retList

# # def moving_average1(period, data):
#   size = len(data)
#   n_groups = (size - period) + 1
#   retList = [0] * n_groups
#   start = 0
#   sum = 0

#   for i in range(n_groups):
#     for j in range(period):
#       sum += data[start + j]
#     retList[i] = int(sum/period)
#     sum = 0
#     start += 1

#   lagList = [0] * (period - 1)
#   retList = lagList + retList

#   return retList

# test = [5,3,2,7,8,1,9,6]
# print(moving_average(3, test))
# print(moving_average1(3, test))

df.to_csv('/content/drive/MyDrive/UCI Conference/ocCovidCountDataset/oc_covid_countAveraged.csv')