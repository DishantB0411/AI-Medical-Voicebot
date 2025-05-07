# Step1: Setup the GROQ API key
import os 
import base64
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# Step2: Convert image to required format
def encoded_image(img_path):
    img_file = open(img_path, "rb")
    encoded_img = base64.b64encode(img_file.read()).decode('utf-8')
    return encoded_img

query = 'Is something wrong with my face?'
model =  'meta-llama/llama-4-scout-17b-16e-instruct'

# Step3: Setup Multimodal LLM
def analyse_img_query(query, model,encoded_img):
    client = Groq()
    message =[
        {
            "role": "user",
            "content": [{"type": "text", "text": query},
                        {"type": "image_url","image_url": {"url": f"data:image/jpeg;base64,{encoded_img}"}}]
        }]

    chat_completion = client.chat.completions.create(
        messages = message,
        model = model
    )
    return chat_completion.choices[0].message.content