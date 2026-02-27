import streamlit as st

# Custom Top Bar CSS
st.markdown("""
    <style>
    .top-bar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #6C63FF; /* Your particular color */
        color: white;
        text-align: center;
        padding: 10px;
        z-index: 999;
        font-weight: bold;
        font-size: 20px;
    }
    /* Adds padding to the top of the app so content doesn't hide under the bar */
    .stApp {
        margin-top: 50px;
    }
    </style>
    <div class="top-bar">OSTEEN NDERITU PORTFOLIO</div>
    """, unsafe_allow_html=True)

st.info("💡 Note: Streamlit's theme (Dark/Light) is controlled by the user in 'Settings'. Custom JS is required to force a toggle button, but you can style your app to match either!")

# CSS for the Horizontal Scroll
st.markdown("""
    <style>
    .scroll-container {
        display: flex;
        overflow-x: auto;
        white-space: nowrap;
        padding: 10px;
        gap: 20px;
    }
    .project-card {
        flex: 0 0 300px; /* Do not shrink, do not grow, stay 300px wide */
        background-color: #262730;
        border-radius: 10px;
        padding: 20px;
        color: white;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Project Data
projects = [
    {"name": "AI Chatbot", "doc": "Built with GPT-4..."},
    {"name": "Data Dashboard", "doc": "Interactive Sales data..."},
    {"name": "Neural Network", "doc": "Image classification..."},
    {"name": "Stock Predictor", "doc": "Time-series analysis..."}
]

# Rendering the Slider
html_cards = "".join([f'<div class="project-card"><h4>{p["name"]}</h4></div>' for p in projects])
st.markdown(f'<div class="scroll-container">{html_cards}</div>', unsafe_allow_html=True)

# Use a selectbox or buttons to show documentation
selected_project = st.selectbox("Select a project to view details:", [p['name'] for p in projects])
project_info = next(p for p in projects if p["name"] == selected_project)

with st.container(border=True):
    st.subheader(f"Documentation: {project_info['name']}")
    st.write(project_info['doc'])
    st.button("View Live Output")

st.divider()
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.header("Education background")
        st.write("**BSc in Data Science**")
        st.caption("Meru University of Science and Technology | 2024 - Present")
        st.write("**KCSE: B**")
        st.caption("Njiiri School | 2020 - 2023")
        st.write("**KCPE: 381/500**")
        st.caption("Moi School Thika | 2009 - 2019")

with col2:
    with st.container(border=True):
        st.header("Language Proficiency")
        st.progress(1.0, text="Python")
        st.progress(0.8, text="SQL")
        st.progress(0.9, text="Excel")

with st.container(border=True):
    st.header("Aspirations & Goals")
    st.write("-> Master Large Language Model Fine-tuning")
    st.write("-> Contribute to Open Source Data Science tools")
    st.write("-> Contribute my expertise to improve healthcare systems")