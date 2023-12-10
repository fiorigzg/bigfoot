import pandas as pd
import math


df = pd.read_csv('bfro_reports_geocoded.csv')
df['year'] = pd.to_datetime(df['date'], format='%Y-%m-%d').dt.year

def get_statistic(json):
  df_filtered = df[(df['year'] >= json['fromYear']) & (df['year'] <= json['toYear'])]
  df_filtered = df_filtered[[json['param']]]
  mean = df_filtered.mean()[json['param']]
  median = df_filtered.median()[json['param']]
  if math.isnan(mean):
    mean = 0
  if math.isnan(median):
    median = 0
  return { "mean": mean, "median": median }
