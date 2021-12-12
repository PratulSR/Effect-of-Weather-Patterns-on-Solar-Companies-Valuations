#Data cleaning and ensuring data quality
# part 1
import pandas as pd
dataset= pd.read_csv("Companies_all_together.csv")
modified_dataset= dataset.fillna(" ")
print(modified_dataset)

# part 2.1
no_date= modified_dataset.drop('Date', 1) #Dropping date column
print(no_date["Canadian Solar"] < 0)
print(no_date["Enphase Energy Inc"] < 0)
print(no_date["First Solar Inc"] < 0)
print(no_date["SolarEdge Technologies Inc"] < 0)
print(no_date["SunPower Corp"] < 0)
print(no_date["Sunrun Inc"] < 0)
print(no_date["Azure Global Ltd"] < 0)
print(no_date["Atlantica Sustainable Infrastructure PLC"] < 0)
print(no_date["JinkoSolar Holdings"] < 0)
print(no_date["Renewable Energy Group"] < 0)

#part 2.2

no_date= modified_dataset.drop('Date', 1) #Dropping date column
print(no_date["Canadian Solar"] > 10000)
print(no_date["Enphase Energy Inc"] > 10000)
print(no_date["First Solar Inc"] > 10000)
print(no_date["SolarEdge Technologies Inc"] > 10000)
print(no_date["SunPower Corp"] > 10000)
print(no_date["Sunrun Inc"] > 10000)
print(no_date["Azure Global Ltd"] > 10000)
print(no_date["Atlantica Sustainable Infrastructure PLC"] > 10000)
print(no_date["JinkoSolar Holdings"] > 10000)
print(no_date["Renewable Energy Group"]> 10000)


# Data aggregates
#1
no_date= modified_dataset.drop('Date', 1) #Dropping date column
max_prices= no_date.max()
print(max_prices)

#2
no_date= modified_dataset.drop('Date', 1) #Dropping date column
min_price= no_date.min()
print(min_price)

#3 - Finding COGR

F= (no_date["Canadian Solar"].iloc[12])
L= (no_date["Canadian Solar"].iloc[189])
N=16 #number of years between 2005 and 2021
COGR = ((L/F) ** (1/N)) -1
COGR_percentage= COGR * 100
print(COGR_percentage)
