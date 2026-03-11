import pandas as pd

def delay_by_airline(df):

    result = df.groupby("AIRLINE")["ARRIVAL_DELAY"].mean().sort_values()

    return result

def delay_by_month(df):

    result = df.groupby("MONTH")["ARRIVAL_DELAY"].mean()

    return result

def busiest_airports(df):

    result = df["ORIGIN_AIRPORT"].value_counts().head(10)

    return result