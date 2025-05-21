import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv(r"D:\Coding\Hackathon\Urban Air Quality and Health Impact Dataset.csv")

df = df.drop(columns=[
    "tempmax", "tempmin", "feelslikemax", "feelslikemin",
    "feelslike", "precipcover", "preciptype", "snow",
    "snowdepth", "winddir", "severerisk", "sunrise", "sunriseEpoch",
    "sunset", "sunsetEpoch", "moonphase", "conditions", "description", "icon",
    "stations", "source", "Temp_Range", "Heat_Index", "Severity_Score",
    "Condition_Code","Season", "datetimeEpoch"
])

df['datetime'] = pd.to_datetime(df['datetime'])

day_encoding = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}

df['Day_Code'] = df['Day_of_Week'].map(day_encoding)

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

df = df.drop(columns=['datetime', 'City', 'Day_of_Week'])

X = df.drop(columns=['Health_Risk_Score'])
Y = df['Health_Risk_Score']

def userInput(start_date,timerange,locationid,hour=12):
    loc_input = []

    for i in range(timerange): # time range = number of days looping through
        future_date = start_date + timedelta(days=i)
        dayofweek = future_date.weekday()
        month = future_date.month
        dayofyear = future_date.timetuple().tm_yday
        loc_input.append([hour,dayofweek,month,dayofyear,locationid])
    return loc_input