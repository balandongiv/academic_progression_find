import json
import streamlit as st

# @st.cache
def load_data():
    with open('data/repo.json') as f:
        data = json.load(f)
    return data