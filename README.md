# How have evolving weather patterns affected the valuations of solar energy companies in the last 20 years

## Contributors
- Pratul Singh Raghava
- Isaac Brooke
- Lorenzo Tamburrino

## The Question
The goal is to link the effects of global warming over a period of 20 years - as most of the companies analysed only went public in this period of time - to the investment trends in the solar energy sector. To do this we decided to focus on getting datasets relevant to the energy sector from a meteorological point of view (temperature) and financial one: data from indexes companies analysed are part of and monthly value of the specific company stock on the indexes

## Relevance
In order to address our question we needed two weather based datasets, and two financial markets based datasets. Historical prices of the largest solar energy companies were required in order to track valuations. The prices of the indexes were then required in order to understand whether these fluctuations in valuations are simply market wide movements, or if the companies are responding in a unique way to changing weather patterns. In order to track these weather patterns we chose to use an EMHIRES solar database, which tracks solar power output as a product of meteorological events, independent from organic growth in demand. Finally, we collected a dataset for renewable energy consumption globally, allowing us to broaden the focus of our question. Comparison between the two meteorological databases will also allow us to separate weather patterns from other factors which may influence renewable energy output. 

## The Stakeholders
We identified three main stakeholders: Solar energy companies, governments and investors. 

Federal Governments & Central Banks: Governments benefit from understanding market sentiment, due to the relationship between stock market performance and the overall health of the economy. As solar energy companies grow as a proportion of the market their influence over macroeconomic trends such as economic growth or inflation will increase. Thus if governments can understand how a solar companies share price may move in the future, they can make more informed monetary policy and microeconomic policy decisions. Our data will build this understanding by providing governments with another data point to understand how solar companies are influenced by weather patterns. By using our data to understand this relationship Governments and Central Banks can make more informed, more accurate, policy decisions. 

Companies: It is important for companies to understand the factors which influence their stock price. In terms of capital raising a company may be able to take advantage of a share price premium to raise more capital at a lower equity cost. A solar energy company will likely have greater visibility into weather patterns and electricity usage going forward. If they can understand the relationship between these trends and their own stock price they are ideally positioned to capitalize on equity premiums and reward their investors. 

Investors: The investment analysis and decisions process of investors is always characterized by a careful analysis of the data of specific company analysed (through financial statements of the company) and the broader market. Our data is focused on delivering an evaluation of the renewables (especially solar) market, showing how it has behaved and what its state has been in a society characterized by increasing temperatures. Therefore we believe that our data analysis will provide further benefits to present and future investors to understand and see how this industry is behaving in the present and has behaved in the past in a societal context characterized by increasing temperatures 


# Index Data Set 
## Metadata

The data is structured in a long data format. A time series in chronological order shows the end of date of each month from October 1959 to August 2021. Each following column is then associated with an index from a different part of the world, with “#N/A N/A” filling in the cell where no data is available. It has a volume of 8173 entries. 

## Data Dictionary

    Field Name	Data Type	Field Length	Description
    
    Date	        Date	        10	        Date where close price was recorded
    Close Price	String	        256	        Price of index (excluding dividends) at market close on the given date
    CCMP Index	String	        256	        Close price at the end of the month for the NASDAQ Index
    NYA Index	String	        256	        Close price at the end of the month for the NYSE Composite Index
    HSI Index	String	        256	        Close price at the end of the month for the Hang Seng Index
    KRX Index	String	        256	        Close price at the end of the month for the KBW Nasdaq Regional Banking Index
    KOSPI Index	String	        256	        Close price at the end of the month for the KOSPI Index (previously the Korea Stock Exchange).
    DAX Index	String	        256	        Close price at the end of the month for the DAX Index
    IBEX Index	String	        256	        Close price at the end of the month for the IBEX Index
    SMI Index	String	        256	        Close price at the end of the month for the Swiss Market Index
    TA-125 Index	String	        256	        Close price at the end of the month for the Tel Aviv 125 Index
    CAC Index	String	        256	        Close price at the end of the month for the CAC 40 Index
    TWSE Index	String	        256	        Close price at the end of the month for theTaiwan Capitalization Weighted Stock Index

## Provenance
This data was originally collected from Bloomberg, which provides data and analytics for financial markets. Bloomberg receives this data directly from securities information processors which parse information into Bloomberg run data centers. As there is no third party involvement the data is both highly secure, and accurate. 
Bloomberg data can be used by students to “research content that integrates their ideas with Bloomberg data” , meaning it can be used for the purposes of this research. 

## Data Quality

The core cleaning task involved reducing the time frame to match that of the Companies dataset. As the first date of the Companies timeline is 01/12/2005, all dates after this were stored in a separate date frame for future analysis. This also accounts for any completeness issues which may have arisen due to missing data. 

By comparing the output of these two functions it can be seen that all missing values have been cleaned from the dataset. Note that the dates column required no cleaning as there were no missing values pre-clean.

A share price (and therefore index price)  must be greater than 0, and so we checked for negative values using the below code:
 
The dates column was dropped from the dataframe as it is not relevant, while the ravel function was used to flatten the data such that the sum function can be used effectively. 
The same logic was applied to values greater than 100,000 as no index for a top 20 securities exchange has ever been priced at greater than 100,000 in the local currency.

Both output a sum of 0, indicating no illogical extreme values to the data.

## Data Aggregates

1. NASDAQ Maximum Monthly Volatility 
 
For the tested aggregate we wanted to test which month, on average, experienced the most volatility for the NASDAQ index. This involved creating a new list for growth rates as an absolute change month on month and adding it to the data frame. I then averaged these rates over the time series, adding this into a dictionary with all the calendar months. The maximum average volatility was found to be October, with an average fluctuation of 6.06% (see output below). As the data is in a dictionary, we can see the average volatility for every month.

2. How much has the NYSE index grown from 1/12/2005?
 
Using the iloc function to index the first and last recorded prices for the NYSE, we then divided them to find the growth rate. We then converted this to a readable percentage.

3. Grouped aggregate: What is the highest recorded price for each index?
 
A simple max function will produce the highest price for each index since the beginning of the time series. As seen below, the output also includes the most recent recorded date.

# Company Dataset

## Data Dictionary

    Field Name	                              Data Type	        Field Length	Description
    
    Date	                                      Date	        10	        The specific day where the closing price was recorded
    Close price (NASDAQ-NYSE Combined)	      Float		                The close price is the last price at which a security traded during the regular trading day
    
    Companies:			
    
    Canadian Solar	                              String	        256	        Canadian Solar Inc. is a publicly traded company that manufactures solar PV modules and runs large scale solar projects
    Enphase Energy Inc	                      String	        256	        Enphase Energy is an American energy technology company. It designs and manufactures software-driven home energy solutions that span solar generation, home energy storage and web-based monitoring and control
    First Solar Inc	                              String	        256	        First Solar, Inc. is an American manufacturer of solar panels, and a provider of utility-scale PV power plants and supporting services that include finance, construction, maintenance and end-of-life panel recycling
    SolarEdge Technologies	                      String	        256	        SolarEdge Technologies, Inc. is an Israel-headquartered provider of power optimizer, solar inverter and monitoring systems for photovoltaic arrays.
    SunPower Corp         	                      String	        256	        SunPower Corporation is an American company specializing in solar power generation and energy storage
    Sunrun Inc	                              String	        256	        Sunrun Inc. is an American provider of residential solar panels and home batteries
    Azure Power Global Ltd	                      String	        256	        Azure Power Global Limited is an independent power producer, a developer and an operator of utility and commercial scale solar PV power plants headquartered in New Delhi, India. The company sells energy to government utilities, and independent industrial and commercial customers in India
    Atlantica Sustainable Infrastructure PLC      String	        256	        Atlantica is a sustainable infrastructure company that owns and manages renewable energy, efficient natural gas, transmission infrastructure and water assets
    JinkoSolar Holdings	                      String	        256	        JinkoSolar Holding Co., Ltd. is currently the world's largest solar panel manufacturer
    Renewable Energy Group	                      String	        256	        Renewable Energy Group is a biodiesel production company headquartered in Ames, Iowa. Increasingly becoming leader in the solar energy sector

## Provenance
This data was originally obtained from Yahoo Finance, which is a media property that provides financial news, data and commentary including stock quotes, press releases, financial reports, and original content. Yahoo Finance makes its data publicly available for download directly on  its website. (Yahoo Finance, n.d.)

---------------------------------------------------------
Yahoo Finance. (n.d.). Retrieved 09 10, 2021, from https://finance.yahoo.com/
---------------------------------------------------------

## Data Quality

I was in charge of getting the data for a pool of leading solar energy listed companies. Initially, I decided to focus on the world’s leading firms in the sector but ended up focusing only on those listed on the American indexes as we have encountered a currency problem; meaning that indexes from other countries had the companies’ stocks valuations in different currencies. I ended up deciding that the best course of action to collect data that would suit my objective would be to collect the monthly stock prices for every company on my list since the IPO (Initial Public Offering) date. I downloaded from Yahoo Finance - which has all the stock price historical information about public companies - 10 datasets (one for each company) that ended up forming my original dataset. Out of the information given to us in the original datasets we only ended up considering the closing price of the stock (monthly) for our analysis as it is the standard benchmark used by investors to track the performance of stock performance over time. Then to put all the information together in one dataset I created a new dataset out of the original with the close price for every company analysed at a specific date (monthly frequency). A problem with this approach was of course that not all the companies were listed on the stock exchanges on the same day, therefore I started counting the dates in the dates column since Jan 1st 2005, date which represents the first public listing within the companies analysed in my sample (largest solar firms in the 2 main American stock exchanges)

## Data Cleaning
1. Given that not all the companies stocks listings started the same day, where on a specific date a company might have already had stock price data (as it has already been listed) another might just have missing values, as it might have not gone public yet. Therefore as visible in part 1 the data quality check resulted in many null values

2. To ensure the removal of these null values I replaced empty/missing spaces with a space. This managed to ensure data quality as it gave me no null values

## Quality & Accuracy Checks

To test the accuracy of my data, I checked if there were any outliers,  given the average stock price in the dataset I checked for any values greater than 5,000 or less than 0 (as a share price always needs to be greater than 0).

1. To ensure no outliers were < 0
To ensure no outliers were below zero (impossible for a share price), I temporarily replaced the empty space I issued in “DATA CLEANING” with a 0. Following this, I tested if each subset of the data frame gave “False” outputs to my input ( Subset < 0).  If this happened it meant that there were no values below zero in my data frame.

2. To ensure no outliers > 10.000
Same process.

## Data Aggregates

1. Grouped aggregate: What is the highest recorded price for each aggregate?

To achieve this I used a max function for each company in my dataset. In this situation, I kept the zeros instead of the spaces for all the null values so that I would only have float values (refer to the “ensure data quality” section for null spaces explanation).
 
 
2. What is the lowest possible share price that has been achieved by any company?

The lowest possible share price from the selected pool was reached by SunPower Corp , $2.57. Today though the company trades at around $22

3. Calculating annual compound rate for Canadian Solar.

I selected Canadian Solar for analysis as it has the highest market capitalisation, and is thus likely to be more influential in the solar energy industry. The annual compound rate is the annual growth rate of an investment over a specified period of time longer than one year. It represents one of the most accurate ways to calculate and determine returns for individual assets, investments, portfolios and anything that can rise or fall in value over time

# Energy Potential Dataset

## Metadata

For the years 1986 to 2015, this dataset includes hourly estimates of an area's energy potential expressed as a percentage of a power plant's maximum output. The data used for this particular project, however, only accounts for the 2005-2015 period 

The overall goal of EMHIRES is to allow users to evaluate the impact of meteorological and climate variability on solar power output in Europe, rather than to mimic the actual trend of solar power production over the last few decades. As a result, hourly solar power generation time series for climatic circumstances from 1986 to 2015 (30 years) are released without taking into account any changes in solar installed capacity. As a result, the installed capacity considered is the same as it was at the end of 2015. However, EMHIRES data should not be compared to real power generation statistics except in the context of the reference year 2015.

## Data Dictionary
    Field	            Data Type	          Field Length      Description	   
    
    Country	            Alphabetical	  2                 The name of the countries from which data was recorded	    
    Hourly_Estimate	    Percentage	          20                Energy potential recorded each hour	    

## Provenance
This data was originally collected and compiled by the European Commission's SETIS program, however the version used in this assignment was retrieved from Kaggle. Whilst this is secondary source data, the version available is the same as from the primary source. 

The European Commission's SETIS is an open-access information website, knowledge management and dissemination system for the European strategic energy technology plan. It helps implement the SET Plan (aims to achieve the EU’s energy and climate goals and make Europe a global leader in clean energy and energy efficiency technologies)  and accounts for its progress and achievements through the monitoring progress report. 

## Data Quality Checks
The data used contained more data than was needed. To combat this a new document was created containing the 96,384 (2005-2015) of 262,944 (1986-2015) records available to suit the time period being observed. 

In an attempt to clean the data, all fields containing NULL/0.0 values were excluded from the data set. This was done using a simple python code which would exclude said records and only print non-blank records.

## Data Aggregates

1.	An anomaly noted was that for country ‘CY’ - Cyprus, during the period of 2005-2015 there was no potential for renewable energy ever recorded. 

2.	During the observation period it can also be observed that Poland had the highest overall renewable energy potential with 20262.59168% by 2015.

3. Additionally, Norway was recorded as having the lowest renewable energy generating potential with a recorded total percentage of 4891% 

# Renewable Energy Dataset

## Metadata

The data shows values for different renewable energy parameters over a timespan of 55 years for each country, continent and the whole world. For each country, there are several different indicators which contain different values for each year since 1960.

## Data Dictionary

    Field Name	  Data Type	          Field Length	  Description
    
    Country Name	  String	          256	          Name of each country
    Country Code	  String	          256	          Abbreviation for each country
    Indicator Name	  String	          256	          Name of each indicator
    Indicator Code	  String	          256	          Abbreviation for each indicator
    EG.FEC.RNEW.ZS	  Floating Point	  15	          Renewable energy consumption (% of total final energy consumption)
    EG.ELC.RNWX.ZS	  Floating Point	  15	          Electricity production from renewable sources, excluding hydroelectric (% of total)
    EG.ELC.RNWX.KH	  Integer	          15	          Electricity production from renewable sources, excluding hydroelectric (kWh)
    EG.ELC.RNEW.ZS	  Floating Point	  15	          Renewable electricity output (% of total electricity output)


## Provenance

The Renewable electricity output and production data was obtained from the International Energy Agency (IEA), an autonomous intergovernmental organisation which conducts independent analysis on the various challenges in the energy production and consumption sector. The IEA primarily obtains this official data from governments directly, but also uses secondary sources like the UN Energy Database and the World Bank. The Renewable Energy consumption data is obtained directly from the World Bank’s SE4ALL Global Tracking Framework which also obtains its data from UN member nations’ governments.

## Data Quality

Cleaning
The cleaning task at hand here was to match the timeframe of the other datasets and hence only values before 2005 were filtered out and not displayed. This was done by skipping the columns representing values outside the desired timeframe. Also, throughout the dataset, any missing values were replaced by zero. The dataset contained much more data for indicators irrelevant to the question at hand, and therefore were excluded in the final data. This was achieved by filtering out the rows whose indicator code matched the ones in question and these rows were then appended to the clean data file.

## Data Quality Checks

Several checks were performed on the cleaned data to ensure quality and accuracy. These checks consisted of verifying data types, detecting missing values and verifying that every value is within its designated range.

1.	To ensure the percentage values are between 0 to 100

We start by skipping the header row and then for each row, checking whether the floating point values are between 0 and 100, since they represent percentage values. If a value is found to be beyond this range, a ValueError is raised explicitly.

2.	To ensure there are no empty values in the dataset

For the whole dataset, we check if any record in any row contains some value and is not simply blank. If a blank value is found, a ValueError is raised explicitly.

3.	To ensure the correct data types for each record

First we check if the headers are of string data type and then for each row, we check whether each value is a floating point or not. If a value is not found to be of float data type, an explicit ValueError is raised.

## Data Aggregates

1.	Calculating the biggest rise and fall in production in consecutive years

Output :
 
We calculate the difference in production values for consecutive years starting from 2000-01 and depending on whether the difference is positive or negative, it is stored as a rise or a drop. At the end, the maximum value of  rise or drop is displayed along with the period of time it took place in. From the output, we see that the biggest rise was in 2010-11 while the biggest drop was seen in 2000-01.

2.	Calculating the Highest Consumption to Production Ratio for Renewable Energy

Output: 

For every row, we calculate the ratio of Renewable Energy Consumption to Renewable Energy Production for each year. At the end, we display the highest such ratio as a percentage along with the year it occurs in. The output shows us that 2008 saw the highest such ratio.

3.	Calculating the Average Renewable Electricity Output for 5-year periods :Grouped Aggregate

Output :
 
For the complete dataset, we divide into 3 different periods of time of roughly 5 years each so as to study the change in average renewable electricity output over these periods. From the output, we clearly see a steady increase in the output..

## Final Dataset

After the data cleaning and data quality checks, the data was transposed by interchanging the column vs row orientation to have the indicator values in vertical columns mapped by their respective year of observation on the rows.

This data, although originally starting from 1960, was filtered out to only the 21st century data since the other datasets contained only recent data since the 2000s. The IEA and World Bank update this dataset every five years but the last updation of data from 2016-2020 has not been completed due to the pandemic and therefore the final data only shows values upto 2015, the last available record of data.

# Integration

## Metadata

    Field Name	                                                                        Data Type	    Field Length    Description
    Year	                                                                                Integer	            4	            The year when the closing price and indicators were recorded
    Date	                                                                                Date	            10	            The specific day when the closing price and indicators were recorded
    CCMP Index	                                                                        String	            256	            Close price at the end of the month for the NASDAQ Index
    NYA Index	                                                                        String	            256	            Close price at the end of the month for the NYSE Composite Index
    HSI Index	                                                                        String	            256	            Close price at the end of the month for the Hang Seng Index
    KRX Index	                                                                        String	            256	            Close price at the end of the month for the KBW Nasdaq Regional Banking Index
    KOSPI Index	                                                                        String	            256	            Close price at the end of the month for the KOSPI Index (previously the Korea Stock Exchange).
    DAX Index	                                                                        String	            256	            Close price at the end of the month for the DAX Index
    IBEX Index	                                                                        String	            256	            Close price at the end of the month for the IBEX Index
    SMI Index	                                                                        String	            256	            Close price at the end of the month for the Swiss Market Index
    TA-125 Index	                                                                        String	            256	            Close price at the end of the month for the Tel Aviv 125 Index
    CAC Index	                                                                        String	            256	            Close price at the end of the month for the CAC 40 Index
    TWSE Index	                                                                        String	            256	            Close price at the end of the month for the Taiwan Capitalization Weighted Stock Index
    Renewable energy consumption (% of total final energy consumption)	                Floating Point	    15	            Renewable energy consumption is the share of renewables energy in total final energy consumption.
    Electricity production from renewable sources, excluding hydroelectric (% of total)	Floating Point	    15	            Electricity production from renewable sources, excluding hydroelectric, includes geothermal, solar, tides, wind, biomass, and biofuels.
    Electricity production from renewable sources, excluding hydroelectric (kWh)	        Integer	            15	            Electricity production from renewable sources, excluding hydroelectric, includes geothermal, solar, tides, wind, biomass, and biofuels.
    Renewable electricity output (% of total electricity output)	                        Floating Point	    15	            Renewable electricity is the share of electricity generated by renewable power plants in total electricity generated by all types of plants.
    Canadian Solar	                                                                        String	            256	            Canadian Solar Inc. is a publicly traded company that manufactures solar PV modules and runs large scale solar projects
    Enphase Energy Inc	                                                                String	            256	            Enphase Energy is an American energy technology company. It designs and manufactures software-driven home energy
    solutions that span solar generation, home energy storage and web-based monitoring and control
    First Solar Inc	                                                                        String	            256	            First Solar, Inc. is an American manufacturer of solar panels, and a provider of utility-scale PV power plants and supporting
    services that include finance, construction, maintenance and end-of-life panel recycling
    SolarEdge Technologies	                                                                String	            256	            SolarEdge Technologies, Inc. is an Israel-headquartered provider of power optimizer, solar inverter and monitoring
    systems for photovoltaic arrays.
    SunPower Corp	                                                                        String	            256	            SunPower Corporation is an American company specializing in solar power generation and energy storage
    Sunrun Inc	                                                                        String	            256	            Sunrun Inc. is an American provider of residential solar panels and home batteries
    Azure Power Global Ltd	                                                                String	            256	            Azure Power Global Limited is an independent power producer, a developer and an operator of utility and commercial
    scale solar PV power plants.
    Atlantica Sustainable Infrastructure PLC	                                        String	            256	            Atlantica is a sustainable infrastructure company that owns and manages renewable energy, efficient natural gas, transmission infrastructure and water assets
    JinkoSolar Holdings	                                                                String	            256	            JinkoSolar Holding Co., Ltd. is currently the world's largest solar panel manufacturer
    Renewable Energy Group	                                                                String	            256	            Renewable Energy Group is a biodiesel production company headquartered in Ames, Iowa. Increasingly becoming leader in the solar energy sector

## Changes

One major change that took place before integration of the datasets was the transposing of the dataset containing renewable energy consumption data so as to get the years as a row header and the various indicators as column headers. This enabled a smooth integration of the multiple datasets with records with the same date being grouped together efficiently using Python.

## Provenance

The Renewable electricity output and production data was obtained from the International Energy Agency (IEA), while the Renewable Energy consumption data is obtained directly from the World Bank’s SE4ALL Global Tracking Framework which also obtains its data from UN member nations’ governments. The Companies dataset was originally obtained from Yahoo Finance, which is a media property that provides financial news, data and commentary including stock quotes, press releases, financial reports, and original content. The Index data was originally collected from Bloomberg, which provides data and analytics for financial markets. Bloomberg receives this data directly from securities information processors which parse information into Bloomberg run data centers. 
