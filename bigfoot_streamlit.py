import streamlit as st
import pandas as pd
import numpy as np
from datetime import date


df = pd.read_csv('bfro_reports_geocoded.csv')
df = df.dropna(subset=['latitude', 'longitude'])

st.markdown('# Bigfoot Sightings streamlit')
st.markdown('Here I will show how dataframes changing by data refactoring and interactive map of all bigfoot sightings.')
st.markdown('## Dataframes visualization')
st.markdown('### Main df before cleaning')
st.dataframe(df, height=500)


df.dropna(inplace=True)
def FtoC(df, col):
  df[col] = (df[col] - 32) * 5/9
  return df

df = FtoC(df, 'temperature_high')
df = FtoC(df, 'temperature_mid')
df = FtoC(df, 'temperature_low')

st.markdown('### Main df after cleaning and F to C conversion')
st.dataframe(df, height=500)


date_df = df[['date']].copy()
date_df.dropna(inplace=True)
date_df['Year'] = pd.to_datetime(date_df['date'],
  format='%Y-%m-%d').dt.year
date_df['Month'] = pd.to_datetime(date_df['date'],
  format='%Y-%m-%d').dt.month
date_df['Day'] = pd.to_datetime(date_df['date'],
  format='%Y-%m-%d').dt.day

this_year = date.today().year
date_df = date_df[date_df['Year'] < this_year]
date_df = date_df[date_df['Year'] > 1957]

month_dict = {
  1: 'January',
  2: 'February',
  3: 'March',
  4: 'April',
  5: 'May',
  6: 'June', 
  7: 'July',
  8: 'August',
  9: 'September',
  10: 'October',
  11: 'November',
  12: 'December'
}
date_df['Month'] = date_df['Month'].map(month_dict)

st.markdown('### Date df')
st.dataframe(date_df, height=500)

st.markdown('## Locations on map')

st.map(
  df,
  latitude='latitude',
  longitude='longitude',
)