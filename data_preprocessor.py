def preprocess_data(df):
    """Preprocess the Yulu dataset."""
    df['day'] = df['datetime'].dt.day_name()
    df['month'] = df['datetime'].dt.month
    df['year'] = df['datetime'].dt.year
    df['hour'] = df['datetime'].dt.hour
    return df