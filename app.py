import streamlit as st
from main import location_encoding, df_with_date
from datetime import datetime
import joblib
import pandas as pd

date_counts = df_with_date['datetime'].value_counts().sort_index()

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

start_date = st.date_input("Start date (must be in September)",
                           datetime(2024, 9, 7),
                           min_value=datetime(2024, 9, 7),
                           max_value=datetime(2024, 9, 21))
end_date = st.date_input("End date (must be in September)",
                         datetime(2024, 9, 14),
                         min_value=datetime(2024, 9, 7),
                         max_value=datetime(2024, 9, 21))

x = st.button(f"Compare {city1} and {city2}")

if x:
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
        dates = city_averages.index.tolist()

        return X, dates

    inputs1, dates1 = data_filtering(df_with_date, code1, start_date, end_date)
    inputs2, dates2 = data_filtering(df_with_date, code2, start_date, end_date)

    pred1 = model.predict(inputs1)
    pred2 = model.predict(inputs2)

    avg_score_1 = sum(pred1) / len(pred1)
    avg_score_2 = sum(pred2) / len(pred2)

    line_chart_data = pd.DataFrame({
        f'{city1}': pred1,
        f'{city2}': pred2
    }, index = dates1)

    st.subheader("Health Risk Score Over Time")

    st.line_chart(line_chart_data)

    st.write(f"Average Health Risk:")
    st.write(f"- {city1}: `{avg_score_1:.2f}`")
    st.write(f"- {city2}: `{avg_score_2:.2f}`")

    winner = city1 if avg_score_1 < avg_score_2 else city2
    st.write(f"{winner} is healthier during this time period.")