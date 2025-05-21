import random

def mock_long_term_predict(inputs):
    """
    Simulates AQI predictions using long-term time features, including day_of_year.

    Parameters:
    - inputs: list of lists with features:
        [hour, dayofweek, month, day_of_year, location_encoded]

    Returns:
    - list of predicted AQI values (floats)
    """
    predictions = []

    for entry in inputs:
        hour, dayofweek, month, day_of_year, location_encoded = entry

        # Base pollution level by location
        base = 50 + (location_encoded * 10)

        # Time-of-day effect: peak around midday
        time_penalty = abs(hour - 12) * 0.7

        # Weekend effect
        weekend_penalty = 8 if dayofweek in [5, 6] else 0

        # Seasonal effect: cleanest in mid-year (June ~ day 172)
        season_offset = abs(day_of_year - 172)  # how far from mid-year
        seasonal_effect = (season_offset / 172) * 10  # max penalty ~10

        # Simulated yearly increase (optional: more pollution over time)
        yearly_trend = day_of_year * 0.05  # e.g., +18 by end of year

        # Random noise
        noise = random.uniform(-5, 5)

        # Final AQI prediction
        aqi = base + time_penalty + weekend_penalty + seasonal_effect + yearly_trend + noise
        predictions.append(round(aqi, 2))

    return predictions