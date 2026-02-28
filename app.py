import streamlit as st
import pandas as pd
import numpy as np
import faiss

from model import load_data
from preprocessing_utils import clean_data, initialize_engine

st.set_page_config(page_title="Spotify Recs", layout="wide")

@st.cache_data
def get_processed_data():
    raw_data = load_data()
    return clean_data(raw_data)

@st.cache_resource
def get_model_assets(_data):
    return initialize_engine(_data)

c_data = get_processed_data()
X_scaled, index = get_model_assets(c_data)

st.image("logo.png", width=130) 
st.title("Spotify Recommendation System")
st.markdown("---")

st.subheader("Step 1: Search for a song")
search_term = st.text_input("Start typing a song or artist name...", placeholder="e.g. Blinding Lights")

if search_term:

    matches = c_data[c_data['artists'].str.contains(search_term, case=False, na=False)].head(20)
    
    if not matches.empty:

        selected_song = st.selectbox("Select the exact match:", options=matches['artists'].tolist())
        
        target_index = matches[matches['artists'] == selected_song].index[0]
        
        st.markdown(f"### Because you liked **{selected_song}**...")
        st.write("Here are 5 similar songs based on audio features:")

        query_vector = X_scaled[target_index : target_index + 1]
        distances, indices = index.search(query_vector, 6)
        
        rec_indices = indices[0][1:]
        
        for i, r_idx in enumerate(rec_indices):
            song_info = c_data.iloc[r_idx]
            
            with st.container():
                col1, col2 = st.columns([0.1, 0.9])
                with col1:
                    st.write(f"### {i+1}")
                with col2:
                    st.markdown(f"**{song_info['name']}**")
                    st.caption(f"Artist: {song_info['artists']} | Album: {song_info['album']}")
                st.markdown("---")
    else:
        st.error("No matches found. Try a different search.")

else:
    st.info("Please enter a song name to see recommendations.")