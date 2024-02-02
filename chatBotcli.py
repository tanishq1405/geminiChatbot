from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables
import os
import google.generativeai as genai
from elevenlabs import generate, play
# from playsound import playsound
# import pyttsx3

# engine = pyttsx3.init()

genconfig = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1
}

api_key=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro',
                              generation_config=genconfig)
# message = input("Enter your message: ")
message = "hello"
# def new_func(model,message):
#         message = input("Enter your message: ")
#         response = model.start_chat(history=[])
#         response = response.send_message(message)
#         responsetext = response.text
#         print(responsetext)

chat = model.start_chat(history=[])
response = chat.send_message("keep your answers less than 200 characters")
while message != "quit":
        message = input("\nEnter your message: ")
        response = chat.send_message(message)
        responsetext = response.text
        print("\n"+responsetext)
        # audio = generate(
        #     text=responsetext ,
        #     voice = "Daniel",
        #     api_key="9b04efabe461bf861032d46553aaac2c",)
        # play(audio)
