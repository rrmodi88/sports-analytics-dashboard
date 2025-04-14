# main.py
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_KEY = "your_api_key"
BASE_URL = "https://v3.football.api-sports.io"

def fetch_live_matches():
    headers = {"x-apisports-key": API_KEY}
    response = requests.get(f"{BASE_URL}/fixtures?live=all", headers=headers)
    return response.json()["response"]

st.title("⚽ Live Sports Analytics Dashboard")
matches = fetch_live_matches()

for match in matches:
    home_team = match["teams"]["home"]["name"]
    away_team = match["teams"]["away"]["name"]
    st.subheader(f"{home_team} vs {away_team}")
    
    # Plot stats
    stats_df = pd.DataFrame(match["statistics"])
    fig = px.bar(stats_df, x="type", y="value", title="Match Statistics")
    st.plotly_chart(fig)
