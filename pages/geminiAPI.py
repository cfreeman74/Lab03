import google.generativeai as genai
import os
import requests
import json
import streamlit as st

#key = st.secrets.get("key")
key = st.secrets["key"]


genai.configure(api_key=key)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
st.write(response.text)

def taller():

    st.header("Who's taller?")
    st.write("Put in the characters of your chioice.")
    st.write("---")



   character1 = st.text_input("Type in a starwars character")
   character2 = st.text_input("Type in another starwars character")


   i = 1
   height1 = "0"
   height2 = "0"
  
  


   while i < 100:
       movie_number = i
       base_url = "https://swapi.dev/api/people/"
       full_url = f"{base_url}{movie_number}/"
       response = requests.get(full_url)
       data = response.json()


       if data["name"] == character1:
           height1 = data["height"]
      
      
       elif data["name"] == character2:
           height2 = data["height"]
      
       else:
           i+=1








   if height1 > height2:
       return f"{character1} is taller!"


   elif height2 > height1:
       return f"{character2} is taller!"


   elif height1 == height2:
       return f"{character1} and {character2} are the same height!"


   else:
       return "We can't tell :("


st.write(taller())
