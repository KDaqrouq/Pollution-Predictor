# Health Risk Score Comparator (Urban U.S. Cities)

A machine learning project that predicts health risk scores for major U.S. cities using air quality and environmental data. The web app includes a City Comparison Tool that lets users compare which city is healthier to live in.

**Model Performance:**  
- R² score: 97%  
- OOB score: 97.2%  

## Limitations

- **Time Range:** The dataset contains only September dates. Predictions are not available for other months or the full year.

## Features

- **City Comparison Tool:** Select any two cities and predict their health risk score over a custom time period (e.g., 7, 14, 30 days).
- **Interactive Streamlit App:** Clean UI allowing non-technical users to simulate predictions without extra data.
- **Simulated Future Forecasts:** Predict Future September health risk using average historical environmental inputs.
- **Feature Engineering:**
  - **Time features:** Encoded day-of-week (`Day_Code`)
  - **Environmental inputs:**  
    - `temp`: Temperature  
    - `dew`: Dew point  
    - `humidity`: Humidity  
    - `precip`: Precipitation  
    - `precipprob`: Precipitation probability  
    - `windgust`: Wind gust speed  
    - `windspeed`: Wind speed  
    - `pressure`: Air pressure  
    - `cloudcover`: Cloud cover  
    - `visibility`: Visibility  
    - `solarradiation`: Solar radiation  
    - `solarenergy`: Solar energy  
    - `uvindex`: UV index    
    - `City_Code`: Encoded city code 
- **Reusable Model Pipeline:** Trained model saved with `joblib` for fast inference.

## Tech Stack

- **Python** (main language)
- **Pandas**, **Scikit-learn**
- **Streamlit** for the web app

## Live Demo

Try the app live: [health-risk-comparison.streamlit.app](https://health-risk-comparison.streamlit.app/)
