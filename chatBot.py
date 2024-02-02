import google.generativeai as ai

class GenAiExeption(Exception):
    """Base class for exceptions in this module."""
    pass

class ChatBot:
    """Chat bot can only have one candidate count"""
    CHATBOT_NAME = "My Gemini AI"

    def __init__(self,api_key):
        self.genai = ai
        self.genai.configure(api_key=api_key)
        self.model = self.genai.GenerativeModel('gemini-pro')
        self.conversation = None
        self._conversation_history = []

        self.preload_conversation()
    
    def send_prompt(self, prompt, temperature=0.1) :
        if temperature < 0 or temperature > 1:
            raise GenAiExeption( 'Temperature must be between e and 1')
        if not prompt:
            raise GenAiExeption('Prompt cannot be empty')
        try :
            response = self.conversation.send_message(
                content=prompt ,
                generation_config=self._generatiom_config(temperature)
            ) ,
            response.resolve()
            return f'{response. text }\n' + '---' * 20
        except Exception as e:
            raise GenAiExeption(e.message)
        
    @property
    def history(self):
        conversation_history = [
            {'role':message.role , 'text': message.parts[0].text} for message in self.conversation.history
        ]
        return conversation_history

    def clear_conversation(self):
        self.conversation = self.model.start_chat(history=[])


    def start_conversation(self):
        self.conversation = self.model.start_chat(history=self._conversation_history)

    def _generatiom_config(slef,temperature):
        return ai.types.GenerationConfig(
            temperature=temperature, 
            candidate_count=1
        )
    
    def _construct_message(self, text, role='user'):
        return {
            'role': role,
            'parts' : [text]
        }

    def preload_conversation(self,conversation_history = None):
        if isinstance(conversation_history,list):
            self._conversation_history = conversation_history
        else:
            self._conversation_history = [
                self._construct_message('From now on, return the output as a json object that can be loaded in Python with the key as \'reply\'. For example, {"text": "<output goes here>"}'),
                self._construct_message('Sure, I can return the output as a regular JSON object with the key as `reply`. Here is an example: {"text": "Your Output"}','model')
            ]
