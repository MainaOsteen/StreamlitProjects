import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("D:\my documents\Y2S2\Data Warehousing for Analytics\Dim_Equipment.csv")
st.dataframe(df)

st.button("Rerun")

@st.cache_data
def transform(df_1):
    df_1 = df_1.filter(items=["one", "two", "three"])
    df_1 = df_1.apply(np.sum, axis=0)
    return df