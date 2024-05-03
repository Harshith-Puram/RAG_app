from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model=genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

st.header("Gemini based chatbot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input: ", key="input")
submit = st.button("Enter the button")

if submit and input:
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(("you", input))
    st.subheader("Response")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("gemini", chunk.text))

st.subheader("Chat History")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")