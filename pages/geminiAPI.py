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

st.header("Which Star Wars character is taller?")
st.write("Put in the characters of your chioice.")
st.write("---")

character1 = st.text_input("Type in a Star Wars character")
character2 = st.text_input("Type in another Star Wars character")

if st.button("Find out who's taller ->"):
    st.write(taller())


    # model = genai.GenerativeModel("gemini-1.5-flash")
    # chat = model.start_chat(
    #     history=[
    #         {"role": "user", "parts": "Hello"},
    #         {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    #     ]
    # )
    # aiResponse = chat.send_message(model.generate_content(message))
    # #response = chat.send_message("I have 2 dogs in my house.")
    # st.write(response.text)

    # st.title("Interactive Chatbot")
    # st.write("Start a conversation with the AI!")
    
    # Initialize the model


chat = model.start_chat(
history=[
    {"role": "user", "parts": "Hello"},
    {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)

# Create the Streamlit app
def main():
    st.title("Star Wars Chatbot")

    user_input = st.text_input("Enter your message:")

    if user_input:
        response = chat.send_message(user_input)
        st.text_area("AI Response:", response.text)

if __name__ == "__main__":
    main()


#st.write(chatbot())

