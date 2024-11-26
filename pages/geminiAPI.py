import google.generativeai as genai
import os
import requests
import json
import streamlit as st

#key = st.secrets.get("key")
key = st.secrets["key"]
st.write(key)

genai.configure(api_key=key)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
st.write(response.text)

