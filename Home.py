import streamlit as st
import requests

api_key = "DEMO_KEY"
url = ("https://api.nasa.gov/planetary/apod?api_"
       "key=DEMO_KEY")

request = requests.get(url)
content = request.json()

st.set_page_config(layout="wide")

date = content["date"]
title = content["title"]
mage_url = content["hdurl"]
explanation = content["explanation"]

st.title(f"NASA Image Of The Day - {date}")

col1, empty, col2 = st.columns([1.5,.125, 1])
with col1:
    st.subheader(title)
    st.image(mage_url)

with col2:
    st.subheader("Explanation")
    st.info(explanation)

print(content)
