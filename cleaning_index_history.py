#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 18:12:24 2021

@author: isaacbrooke
"""
import pandas as pd
import numpy as np
#pd.options.mode.chained_assignment = None

file = 'Index_history_rerun_again.csv'

df = pd.read_csv(file)

df['Dates'] = pd.to_datetime(df['Dates'])

early_dates = df['Dates'] > '2005-12-1'

trimmed_dates = df.loc[early_dates]

        
## Data Quality: check if any values are <0 or >1,000,000

print(np.sum((trimmed_dates.drop('Dates', 1) > 100000).values.ravel()))


 ## Grouped-Aggregates: what is the highest historical price for each index?   
#max_prices = trimmed_dates.max()
#print("max prices are:")
#print(max_prices)

##Aggregates: which month had the highest volatility on the NASDAQ Index

first_line = True
growth_rates = [0]

for index1 in trimmed_dates['CCMP Index']:
    if first_line:
        previous_month = index1
        first_line = False
    else:
        growth_rates.append(abs(index1/previous_month - 1)) #Calculate the absolute change from the previous month
        previous_month = index1

trimmed_dates['Growth Rates'] = growth_rates

count_months = 1
months = []

while count_months < 13:
    month_df = trimmed_dates['Dates'].dt.month == count_months
    month_df = trimmed_dates.loc[month_df]
    months.append(month_df['Growth Rates'].mean()) #average the change for each month across the time series
    count_months += 1

#print(months)
months_tidy = [f'{i*100:.2f}%' for i in months] #convert the months output into a readable percentage
calendar_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#print(months_tidy)
#print(trimmed_dates)

months_dict = dict(zip(calendar_months, months_tidy))
most_volatile = max(months_dict, key=months_dict.get) #the most volatile month has the highest percentage

#print(most_volatile, months_dict[most_volatile])
#print(months_dict)


## Aggregates: how much has nyse grown since 2005?

growth = trimmed_dates['NYA Index'].iloc[-1] / trimmed_dates['NYA Index'].iloc[0] -1
growth_percentage = "{:.1%}".format(growth)

print(growth_percentage)


# total_growth = trimmed_dates['NYSE Growth Rates'].iloc[0] / trimmed_dates['NYSE Growth Rates'].iloc[-1]
# print(total_growth)








 








