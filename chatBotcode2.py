from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables
import gradio as gr
import os
import google.generativeai as genai

apikey = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=apikey)

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

    def respond(message, chat_history):
        response = chat.send_message(message)
        responsetext = response.text
        chat_history.append((message, responsetext))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()