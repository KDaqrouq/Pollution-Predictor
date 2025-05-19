import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv(r"D:\Coding\Hackathon\Urban Air Quality and Health Impact Dataset.csv")

location_mapping = {
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

def userInput(start_date,timerange,locationid,hour=12):
    loc_input = []

    for i in range(timerange): # time range = number of days looping thru
        future_date = start_date + timedelta(days=i)
        dayofweek = future_date.weekday()
        month = future_date.month
        dayofyear = future_date.timetuple().tm_yday
        loc_input.append([hour,dayofweek,month,dayofyear,locationid])
    return loc_input