import google.generativeai as genai
import os
import streamlit as st

key = st.secrets["key"]

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)