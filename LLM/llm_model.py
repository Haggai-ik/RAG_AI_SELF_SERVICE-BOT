from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq


class llm_model:
    def __init__(self,model_name,api_key,temperature,convert_system_message_to_human):
        self.model_name = model_name
        self.api_key = api_key
        self.temperature = temperature
        self.convert_system_message_to_human = convert_system_message_to_human
        self.model = None
    
    def initialize_model(self):
        self.model =ChatGoogleGenerativeAI(model=self.model_name,
                                           google_api_key=self.api_key,
                            temperature=self.temperature,convert_system_message_to_human=self.convert_system_message_to_human)

        return self.model 
    

class groq_model:
    def __init__(self,model_name,api_key,temperature):
        self.model_name = model_name
        self.api_key = api_key
        self.temperature = temperature
       
    
    def initialize_model(self):
        model = ChatGroq(temperature=self.temperature, groq_api_key=self.api_key, model_name=self.model_name)

        return model 
    
   

    