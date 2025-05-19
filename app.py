import streamlit as st
from main import userInput, location_mapping
from datetime import datetime
from fakemodel import mock_long_term_predict
import pandas as pd

st.title("Comparing Air Quality")

locA_input = st.selectbox(
    "What is the first location?",
    location_mapping.keys(),
)
print(locA_input)
locaB_input = st.selectbox(
    "What is the second location?",
    location_mapping.keys(),
)

timerange_input = st.selectbox(
    "Over how long?",
    ("Week", "Month", "Year"),
)

today = datetime.today()

def timeRange(time):
    if time == "Week":
        return 7
    elif time == "Month":
        return 30
    elif time == "Year":
        return 365

period = timeRange(timerange_input)

x = st.button(f"Compare {locA_input} and {locaB_input}")

if x:
    locationA_inputs = userInput(today,period,location_mapping[locA_input])
    locationB_inputs = userInput(today,period,location_mapping[locaB_input])

    aqi_A = mock_long_term_predict(locationA_inputs)
    aqi_B = mock_long_term_predict(locationB_inputs)

    avg_A = sum(aqi_A) / len(aqi_A)
    avg_B = sum(aqi_B) / len(aqi_B)

    dates = [(today - pd.Timedelta(days=i)).strftime("%Y-%m-%d") for i in range(period)][::-1]

    aqi_data = pd.DataFrame({
        f"{locA_input}": aqi_A,
        f"{locaB_input}": aqi_B
    }, index=dates)

    st.subheader("AQI Over Time")

    st.line_chart(aqi_data)

    st.write(f"{locA_input} has an average pollution score of {avg_A:.2f} and {locaB_input} has an average pollution score of {avg_B:.2f}.")

    if aqi_A < aqi_B:
        st.write(f"{locA_input} is the cleaner city!")
    else:
        st.write(f"{locaB_input} is the cleaner city!")