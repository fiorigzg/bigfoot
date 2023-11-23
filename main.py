import streamlit as st
import pandas as pd


def load_data():
    data = pd.read_csv("data/bfro_reports.csv")
    return data


st.title("Bigfoot reports")

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')    