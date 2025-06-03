import streamlit as st
from main import location_encoding, df, df_with_date
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
)

start_date = st.date_input("Start date (must be in September)", datetime(2024, 9, 1), min_value=datetime(2024, 9, 1))
end_date = st.date_input("End date (must be in September)", datetime(2024, 9, 7), max_value=datetime(2024, 9, 30))

if start_date.month != 9 or end_date.month != 9:
    st.warning("Please make sure the date is in September or the result may be inaccurate!")
else:
    city_averages = df.groupby('City_Code').agg({
        'temp': 'mean',
        'dew': 'mean',
        'humidity': 'mean',
        'precip': 'mean',
        'precipprob': 'mean',
        'windgust': 'mean',
        'windspeed': 'mean',
        'pressure': 'mean',
        'cloudcover': 'mean',
        'visibility': 'mean',
        'solarradiation': 'mean',
        'solarenergy': 'mean',
        'uvindex': 'mean',
        'Day_Code': 'mean',
        'Health_Risk_Score': 'mean'
    }).round(3)

    code1 = location_encoding[city1]
    code2 = location_encoding[city2]

    def prepare_model_features(city_code):
        row_df = city_averages.loc[[city_code]]
        df = row_df.drop(columns=['Health_Risk_Score'])
        df['City_Code'] = df.index
        return df

    inputs1 = prepare_model_features(code1)
    inputs2 = prepare_model_features(code2)

    pred1 = model.predict(inputs1)
    pred2 = model.predict(inputs2)

    avg1_score = pred1[0]
    avg2_score = pred2[0]

    st.markdown(f"Average Health Risk:")
    st.markdown(f"- {city1}: `{avg1_score:.2f}`")
    st.markdown(f"- {city2}: `{avg2_score:.2f}`")

    winner = city1 if avg1_score < avg2_score else city2
    st.success(f"{winner} is healthier during this time period.")