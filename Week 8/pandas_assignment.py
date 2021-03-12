import pandas as pd
import numpy as np
import datetime


def transform():
    df_old = pd.read_csv('data.csv')
    df = df_old[['Created Date', 'Closed Date', 'Borough', 'Descriptor', 'Complaint Type', 'Agency', 'Longitude', 'Latitude', 'Status']]
    df['Created Date'] = pd.to_datetime(df['Created Date'], format='%m/%d/%Y %I:%M:%S %p')
    df['Closed Date'] = pd.to_datetime(df['Closed Date'], format='%m/%d/%Y %I:%M:%S %p')
    df['processing_time'] = df['Closed Date'] - df['Created Date']
    df['start_time_window'] = df['Created Date'].apply(lambda x: x.hour)
    return df.to_csv('output1.csv', index=False)

transform()
