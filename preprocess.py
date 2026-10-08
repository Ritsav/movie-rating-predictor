import numpy as np
import pandas as pd

# Preprocessing logic of data

def convert_weather_units(df):
    # weather columns are normalized, multiply by the max used in the dataset docs
    df['temp'] = df['temp'] * 41        # celsius
    df['atemp'] = df['atemp'] * 50      # celsius (feels like)
    df['hum'] = df['hum'] * 100         # percent
    df['windspeed'] = df['windspeed'] * 67

    return df

def add_cyclical(df, column, period):
    # month 12 and month 1 are neighbours, sin/cos keeps that closeness
    df[f'{column}_sin'] = np.sin(2 * np.pi * df[column] / period)
    df[f'{column}_cos'] = np.cos(2 * np.pi * df[column] / period)

    return df

def convert_date(df):
    # convert the str date column into datetime
    df['dteday'] = pd.to_datetime(df['dteday'])

    return df
