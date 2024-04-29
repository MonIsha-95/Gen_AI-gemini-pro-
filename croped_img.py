
# from PIL import Image

# def crop_image(input_path, output_path, left, top, right, bottom):
#     # Open the image file
#     input_path ='th.jpg'
#     img = Image.open(input_path)

#     # Crop the image
#     cropped_img = img.crop((left, top, right, bottom))

#     # Save the cropped image
#     cropped_img.save(output_path)

# # Example usage:
# input_image_path = "input_image.jpg"
# output_image_path = "output2_image.jpg"

# # Define the crop coordinates (left, top, right, bottom)
# crop_coordinates = (100, 50, 400, 300)

# # Crop the image
# crop_image(input_image_path, output_image_path, *crop_coordinates)



from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
import os

load_dotenv()
api_key =os.getenv("OPEN_API_KEY")
chat_model =ChatOpenAI(openai_api_key = api_key)
result = chat_model.predict("hello")
print(result)