import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv(r"D:\Coding\Hackathon\Urban Air Quality and Health Impact Dataset.csv")

predict = 'Health_Risk_Score' # the variable im training my model to predict

essential_vars = [
    "datetime",         # time reference
    "City",             # location
    "temp",             # average temperature
    "humidity",         # humidity level
    "dew",              # dew point
    "windgust",         # wind gust speed
    "windspeed",        # average wind speed
    "pressure",         # atmospheric pressure
    "cloudcover",       # cloud cover %
    "visibility",       # visibility in miles
    "uvindex",          # UV index
    "precip",           # total precipitation
    "precipprob",       # probability of precipitation
    "solarradiation",   # solar radiation
    "solarenergy",      # solar energy
    "Month",            # the month the data was recorded in
    "Day_of_Week",      # which day of the week it is
    "Is_Weekend",       # True if the day is on a weekend else False
] # the variables I choose to train my model on from the dataset

location_encoding = {
    'New York City' : 0,
    'Philadelphia' : 1,
    'Los Angeles' : 2,
    'Phoenix' : 3,
    'Houston' : 4,
    'San Antonio' : 5,
    'San Diego' : 6,
    'Dallas' : 7,
    'Chicago' : 8,
    'San Jose' : 9
}

df['City_Code'] = df['City'].map(location_encoding)

def userInput(start_date,timerange,locationid,hour=12):
    loc_input = []

    for i in range(timerange): # time range = number of days looping through
        future_date = start_date + timedelta(days=i)
        dayofweek = future_date.weekday()
        month = future_date.month
        dayofyear = future_date.timetuple().tm_yday
        loc_input.append([hour,dayofweek,month,dayofyear,locationid])
    return loc_input