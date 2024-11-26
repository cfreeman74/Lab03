import google.generativeai as genai
import os
import requests
import json
import streamlit as st

#key = st.secrets.get("key")
key = st.secrets["key"]


genai.configure(api_key=key)

model = genai.GenerativeModel("gemini-1.5-flash")


def taller():
    if character1 and character2:
        base_url = "https://swapi.dev/api/people/"
        height1 = None
        height2 = None
        for id in range(1,83):
            response = requests.get(f"{base_url}{id}")
            data = response.json()
            if data["name"].lower() == character1.lower():
                height1 = data["height"]
            if data["name"].lower() == character2.lower():
                height2 = data["height"]

            if height1 and height2:
                break
        if height1 and height2:

            if int(height1) > int(height2):
                result = f"{character1} is taller than {character2}!"
                st.success(result)


            elif int(height2) > int(height1):
                result = f"{character2} is taller than {character1}!"
                st.success(result)

            elif int(height1) == int(height2):
                result = f"{character1} and {character2} are the same height!"
                

            else:
                result= "We can't tell :("
                st.info(result)
            return storage(result)
def storage(result):
    prompt = f"Write a Star Wars themed story about the comparison: {result} Make it exciting!"
    response = model.generate_content(prompt)
    st.write(response.text)

def chatbot():
    # model = genai.GenerativeModel("gemini-1.5-flash")
    # chat = model.start_chat(
    #     history=[
    #         {"role": "user", "parts": "Hello"},
    #         {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    #     ]
    # )
    # response = chat.send_message("I have 2 dogs in my house.")
    # st.write(response.text)

    st.title("Interactive Chatbot")
    st.write("Start a conversation with the AI!")

    # Chat interface
    if "history" not in st.session_state:
        st.session_state.history = [
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ]

    for msg in st.session_state.history:
        if msg["role"] == "user":
            st.text_input("You:", value=msg["parts"], key=f"user_{msg['parts']}", disabled=True)
        else:
            st.text_area("Bot:", value=msg["parts"], key=f"bot_{msg['parts']}", disabled=True)

    user_input = st.text_input("Your message:")
    if st.button("Send"):
        if user_input:
            # Append user input to history
            st.session_state.history.append({"role": "user", "parts": user_input})

            # Generate a response
            response = chat.send_message(user_input)
            st.session_state.history.append({"role": "model", "parts": response.text})

            # Clear input box
            st.experimental_rerun()


st.header("Who's taller?")
st.write("Put in the characters of your chioice.")
st.write("---")

character1 = st.text_input("Type in a starwars character")
character2 = st.text_input("Type in another starwars character")

if st.button("Find out who's taller"):
    st.write(taller())

