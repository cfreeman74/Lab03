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

st.title("Which Star Wars character is taller?")
st.write("Put in the characters of your chioice.")
st.write("---")

character1 = st.text_input("Enter the first Star Wars character: ")
character2 = st.text_input("Enter the second Star Wars character: ")

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

st.markdown("""
<div class="post-game-conference">
  <h2>Post-Game Press Conference:</h2>
  <p>The local Pokémon master was in attendance for the battle. Ask him any questions about the fight!</p>

  <div class="question">
    <img src="pokemon_trainer.png" alt="Pokémon Trainer">
    <p>What Pokémon type is Fezandipiti?</p>
  </div>

  <div class="answer">
    <img src="pokemon_trainer.png" alt="Pokémon Trainer">
    <p>Fezandipiti is a Fairy and Poison-type Pokémon.</p>
  </div>

  <form>
    <input type="text" placeholder="Enter your question here:">
    <button type="submit">▶</button>
  </form>
</div>
""", unsafe_allow_html=True)


chat = model.start_chat(
history=[
    {"role": "user", "parts": "Hello"},
    {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)

# Create the Streamlit app
st.set_page_config(page_title="Pokémon Battle Chat", layout="centered")

    # Page header
st.markdown(
        """
        <div style="text-align: center; font-size: 32px; font-weight: bold; margin-bottom: 20px;">
            Post-Game Press Conference
        </div>
        <div style="text-align: center; font-size: 18px; color: gray;">
            The local Pokémon master was in attendance for the battle. Ask him any questions about the fight!
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Chat interface
user_input = st.text_input(
        "Enter your question here:",
        placeholder="Type your question...",
        label_visibility="hidden"
    )

if user_input:
        # Get response from AI
    response = chat.send_message(user_input)

        # Display chat history
    st.markdown(
            f"""
            <div style="margin: 20px 0; padding: 10px; border: 1px solid #ddd; border-radius: 5px;">
                <b>Pokémon Trainer</b>: {user_input}
                <br><br>
                <b>Pokémon Trainer</b>: {response.text}
            </div>
            """,
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()

# def main():
#     st.header("Star Wars Chatbot")

#     user_input = st.text_input("Enter your question:")

#     if user_input:
#         response = chat.send_message(user_input)
#         st.text_area("AI Response:", response.text)

# if __name__ == "__main__":
#     main()


#st.write(chatbot())

