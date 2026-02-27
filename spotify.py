import streamlit as st
from streamlit_option_menu import option_menu

# 1. Create the navbar
selected = option_menu(
    menu_title=None,       # No title for a horizontal navbar
    options=["Home", "Library", "Search", "Settings"], 
    icons=["house", "music-note-beamed", "search", "gear"], # Bootstrap icons
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal",
    styles= {
        "icon": {"color": "#FFFFFF", "font-size": "20px"},
        "nav-link": {"--hover-color": "gray"},
        "nav-link-selected": {"background-color": "#1DB854"}

    }
)

# 2. Display content based on selection
if selected == "Home":
    st.title(f"Welcome to {selected}")
    st.write("This is your main dashboard.")

if selected == "Library":
    st.title("Your Spotify Library")
    # Insert your Spotify API logic here


