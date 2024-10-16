import pandas as pd

def load_data(file_path):
    """Load the Yulu dataset from a CSV file."""
    df = pd.read_csv(file_path)
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df