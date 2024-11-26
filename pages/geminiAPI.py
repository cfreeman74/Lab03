import google.generativeai as genai
import os
import streamlit as st

export API_KEY=<"AIzaSyCIvvMoX4aMLXKVIkm9snaZ-GuQL2aR9zo">

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)