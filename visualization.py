import matplotlib.pyplot as plt
import seaborn as sns

def plot_hourly_distribution(df):
    """Plot the average hourly distribution of bike rentals."""
    plt.figure(figsize=(12, 6))
    df.groupby(df['datetime'].dt.hour)['count'].mean().plot(kind='line', marker='o')
    plt.title("Average Hourly Distribution of Bike Rentals")
    plt.xlabel("Hour of Day")
    plt.ylabel("Average Count")
    plt.xticks(range(0, 24))
    plt.grid(True)
    return plt

def plot_seasonal_distribution(df):
    """Plot the distribution of bike rentals across seasons."""
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='season', y='count', hue='workingday')
    plt.title("Distribution of Bike Rentals Across Seasons")
    plt.xlabel("Season")
    plt.ylabel("Count")
    plt.grid(True)
    return plt

def plot_weather_impact(df):
    """Plot the impact of weather on bike rentals."""
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='weather', y='count')
    plt.title("Impact of Weather on Bike Rentals")
    plt.xlabel("Weather Condition")
    plt.ylabel("Count")
    plt.grid(True)
    return plt