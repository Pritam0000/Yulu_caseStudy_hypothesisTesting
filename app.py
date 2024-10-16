import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data
from data_preprocessor import preprocess_data
from visualization import plot_hourly_distribution, plot_seasonal_distribution, plot_weather_impact
from analysis import perform_mann_whitney_test, perform_kruskal_wallis_test

# Load and preprocess data
df = load_data('bike_sharing.csv')
df = preprocess_data(df)

# Streamlit app
st.title('Yulu Bike Rental Analysis')

# Overview
st.header('Dataset Overview')
st.write(df.head())
st.write(f"Dataset shape: {df.shape}")

# Visualizations
st.header('Visualizations')

# Hourly distribution
st.subheader('Average Hourly Distribution of Bike Rentals')
fig_hourly = plot_hourly_distribution(df)
st.pyplot(fig_hourly)

# Seasonal distribution
st.subheader('Distribution of Bike Rentals Across Seasons')
fig_seasonal = plot_seasonal_distribution(df)
st.pyplot(fig_seasonal)

# Weather impact
st.subheader('Impact of Weather on Bike Rentals')
fig_weather = plot_weather_impact(df)
st.pyplot(fig_weather)

# Statistical Analysis
st.header('Statistical Analysis')

# Working Day vs Non-Working Day
st.subheader('Working Day vs Non-Working Day')
stat_workingday, p_workingday = perform_mann_whitney_test(df, 'workingday', 1, 0)
st.write(f"Mann-Whitney U test statistic: {stat_workingday}")
st.write(f"p-value: {p_workingday}")
if p_workingday < 0.05:
    st.write("There is a significant difference in bike rentals between working days and non-working days.")
else:
    st.write("There is no significant difference in bike rentals between working days and non-working days.")

# Weather Impact
st.subheader('Weather Impact')
stat_weather, p_weather = perform_kruskal_wallis_test(df, 'weather')
st.write(f"Kruskal-Wallis H-test statistic: {stat_weather}")
st.write(f"p-value: {p_weather}")
if p_weather < 0.05:
    st.write("There is a significant difference in bike rentals across different weather conditions.")
else:
    st.write("There is no significant difference in bike rentals across different weather conditions.")

# Seasonal Impact
st.subheader('Seasonal Impact')
stat_season, p_season = perform_kruskal_wallis_test(df, 'season')
st.write(f"Kruskal-Wallis H-test statistic: {stat_season}")
st.write(f"p-value: {p_season}")
if p_season < 0.05:
    st.write("There is a significant difference in bike rentals across different seasons.")
else:
    st.write("There is no significant difference in bike rentals across different seasons.")

# Conclusions
st.header('Conclusions')
st.write("""
Based on the analysis:
1. The demand for bike rentals shows clear hourly patterns, with peaks during commute hours.
2. Seasonal variations significantly impact bike rental demand.
3. Weather conditions play a crucial role in determining the number of bike rentals.
4. There is a statistical difference in bike rentals between working days and non-working days.
""")

# Recommendations
st.header('Recommendations')
st.write("""
1. Optimize bike availability during peak hours, especially during morning and evening commutes.
2. Implement seasonal pricing strategies to balance demand across different seasons.
3. Develop weather-based promotional campaigns to encourage rentals during favorable conditions.
4. Consider different strategies for working days and non-working days to maximize utilization.
""")