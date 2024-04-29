from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
import google.generativeai as genai

# genai.configure(api_key="AIzaSyDINUUOkQhz0c4otr32_kaFJkf6BBLkcgE")
genai.configure(api_key =os.getenv("GOOGLE_API_KEY"))

#function to load Gemini-pro model and get responses

model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(questions):
    response= model.generate_content(questions)
    
    
## initailize our streamlit app
st.set_page_config(page_title="Gemini Q&A demo")
st.header("Gemini_applications")
inputs = st.text_input("Inputs",key='inputs')
submit = st.button("Submit ")
#when submit is click

if submit:
    response = get_gemini_response(inputs)
    st.subheader("The Response is ")
    st.write(response)