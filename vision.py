# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image


import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app

def crop_image(input_path, output_path, left, top, right, bottom):
    # Open the image file
    input_path ='IMG_20231214_185344_877.jpg'
    img = Image.open(input_path)

    # Crop the image
    cropped_img = img.crop((left, top, right, bottom))

    # Save the cropped image
    cropped_img.save(output_path)

# Example usage:
input_image_path = "input_image.jpg"
output_image_path = "output_image.jpg"

# Define the crop coordinates (left, top, right, bottom)
crop_coordinates = (100, 50, 400, 300)

# Crop the image
croped_image= crop_image(input_image_path, output_image_path, *crop_coordinates)

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Ans the propmt")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)