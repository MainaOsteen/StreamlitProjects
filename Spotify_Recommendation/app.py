import streamlit as st
import streamlit_option_menu as option_menu
from model import load_data


st.title("Spotify Recommendation System")
st.markdown("---")

st.sidebar.title("Settings")
st.dataframe(load_data)
