import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):

    df = df.dropna(subset=["AIRLINE","ORIGIN_AIRPORT","DESTINATION_AIRPORT"])

    df["ARRIVAL_DELAY"] = df["ARRIVAL_DELAY"].fillna(0)
    df["DEPARTURE_DELAY"] = df["DEPARTURE_DELAY"].fillna(0)

    return df