import streamlit as st
from main import location_encoding, df_with_date
from datetime import datetime
import joblib
import pandas as pd

model = joblib.load("healthriskscore_model.pkl")

st.title("Comparing Health Risk Score Across Two Cities")

city1 = st.selectbox(
    "What is the first location?",
    location_encoding.keys(),
)

city2 = st.selectbox(
    "What is the second location?",
    location_encoding.keys(),
    index=1
)

start_date = st.date_input("Start date (must be in September)", datetime(2024, 9, 1), min_value=datetime(2024, 9, 1))
end_date = st.date_input("End date (must be in September)", datetime(2024, 9, 14), max_value=datetime(2024, 9, 30))

if start_date.month != 9 or end_date.month != 9:
    st.warning("Please make sure the date is in September or the result may be inaccurate!")
else:
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    code1 = location_encoding[city1]
    code2 = location_encoding[city2]

    def data_filtering(df, city_code, start_date, end_date):
        filtered_df = df[(df['datetime'] >= start_date) & (df['datetime'] <= end_date)]

        city_data = filtered_df[filtered_df['City_Code'] == city_code]

        city_averages = city_data.groupby('datetime').agg({
            'temp': 'mean',
            'dew': 'mean',
            'humidity': 'mean',
            'precip': 'sum',
            'precipprob': 'max',
            'windgust': 'max',
            'windspeed': 'mean',
            'pressure': 'mean',
            'cloudcover': 'mean',
            'visibility': 'min',
            'solarradiation': 'mean',
            'solarenergy': 'sum',
            'uvindex': 'max',
            'Day_Code': 'first',
            'City_Code': 'first'
        }) # used min or max for values where extreme values affect health risk more significantly.
        # sum for values that are accumulative throughout the day

        X = city_averages

        return X

    inputs1 = data_filtering(df_with_date, code1, start_date, end_date)
    inputs2 = data_filtering(df_with_date, code2, start_date, end_date)

    print(inputs1)
    pred1 = model.predict(inputs1)
    pred2 = model.predict(inputs2)

    print(pred1)

    #avg1_score = pred1[0]
    #avg2_score = pred2[0]

    #st.markdown(f"Average Health Risk:")
    #st.markdown(f"- {city1}: `{avg1_score:.2f}`")
    #st.markdown(f"- {city2}: `{avg2_score:.2f}`")

    #winner = city1 if avg1_score < avg2_score else city2
    #st.success(f"{winner} is healthier during this time period.")