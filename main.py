import pandas as pd

df = pd.read_csv(r"C:\Users\Taysir\khaled\Pollution-Predictor\Urban Air Quality and Health Impact Dataset.csv")

df = df.drop(columns=[
    "tempmax", "tempmin", "feelslikemax", "feelslikemin",
    "feelslike", "precipcover", "preciptype", "snow",
    "snowdepth", "winddir", "severerisk", "sunrise", "sunriseEpoch",
    "sunset", "sunsetEpoch", "moonphase", "conditions", "description", "icon",
    "stations", "source", "Temp_Range", "Heat_Index", "Severity_Score",
    "Condition_Code","Season", "datetimeEpoch"
]) # dropped these columns because they are not needed for the model

df['datetime'] = pd.to_datetime(df['datetime'])
# encoded location and day of the week because they are categorical and the model needs quantitative data
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

df_with_date = df.drop(columns=['City', 'Day_of_Week', 'Month','Is_Weekend'])

df = df.drop(columns=['datetime', 'City', 'Day_of_Week', 'Month','Is_Weekend'])
# decided to drop month because the in the dataset the month is constant (Sept.)
# decided to drop Is Weekend after parameter tuning and finding increased model accuracy

X = df.drop(columns=['Health_Risk_Score'])
Y = df['Health_Risk_Score']