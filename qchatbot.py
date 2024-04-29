from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
import google.generativeai as genai 
 
genai.configure(api_key =os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Q&A demo")
st.header("Gemini LLM Application")

#Initialize session for chat history generation

if 'chat_history' not in st.session_state:
    st.session_state["chat_history"]=[]
    
input = st.text_input("Input",key='input')
submit=st.button("Click")

if (submit and input):
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(input)
    st.subheader("The Response is : ")
    
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(chunk.text)
st.subheader("The Chat Hsitory")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")