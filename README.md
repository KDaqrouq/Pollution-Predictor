# Health Risk Score Comparator (Urban U.S. Cities)

A machine learning project that predicts health risk scores for major U.S. cities using air quality and environmental data. This repository includes a **City Comparison Tool** that lets users compare which city is healthier to live in.

**Model Performance:**  
- R² score: 97%  
- OOB score: 97.2%  

## Features

- **City Comparison Tool:** Select any two cities and predict their health risk score over a custom September time period (e.g., 7, 14, 30 days).
- **Interactive Streamlit App:** Clean UI allowing non-technical users to simulate predictions without extra data.
- **Simulated Future Forecasts:** Predict future September health risk using average historical environmental inputs.
- **Feature Engineering:**
  - Time features: `day_of_year`, `day_code`, `hour`
  - Environmental inputs: `humidity`, `temp`, `uvindex`, `windspeed`, `cloudcover`
  - Encoded city and day-of-week using numerical codes
- **Reusable Model Pipeline:** Trained model saved with `joblib` for fast inference.

## Tech Stack

- **Python** (main language)
- **Pandas**, **NumPy**, **Scikit-learn**
- **Streamlit** for the web app
- **Joblib** for model serialization

## Live Demo

Try the app live: [health-risk-comparison.streamlit.app](https://health-risk-comparison.streamlit.app/)

## How It Works

This project uses a **Random Forest Regressor** to estimate a city's **daily health risk score** based on urban environmental factors and time-based variables. Users can simulate and compare the health risk between **two cities** across a selected **September time range**.
