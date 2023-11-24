# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:46:00 2023

@author: star26
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
df1=pd.read_excel(r'\\192.168.60.77\dataset_share\BAM_India_SPOT.xls')
df1.columns

## drop all columns except date column and target column
 
df1.drop(['Price series', 'Price Status', 'Unit of Measure',
       'Mid Price', 'High Price'] , inplace=True ,axis=1)

df1=df1[df1['Date']>'2023-02-22 00:00:00']
data = df1.set_index('Date')


def simple_exponential_smoothing(df):



    #df.Month = pd.to_datetime(df.Month)

    # Import function
    from statsmodels.tsa.holtwinters import SimpleExpSmoothing

    model = SimpleExpSmoothing(data)
    fit = model.fit()
    fcast = fit.forecast(8)
    # Plot time series and forecasted predictions
    fig = plt.figure(figsize=(14,6))
    plt.plot(data, color='black', label='Observed')
    fcast.plot(color='red', label='Forecast')
    plt.title('Simple Exponential Smoothing Predictions')
    plt.xlabel('Date')
    plt.ylabel('Kegs Produced')
    plt.legend()
    plt.show()

    
simple_exponential_smoothing(df1)    

