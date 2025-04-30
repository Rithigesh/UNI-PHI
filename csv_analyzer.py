import pandas as pd

# Function to load and analyze a CSV file
def load_and_analyze_csv(file_path):
    df = pd.read_csv(file_path)
    return df
