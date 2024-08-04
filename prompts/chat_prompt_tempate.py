from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder

class chatprompt:
    def __init__(self, context_prompt):
          self.context_prompt =context_prompt
          self.context =None
          
    def use_chat_template(self):
        self.context =   ChatPromptTemplate.from_messages(
         [
            ("system", self.context_prompt),
             MessagesPlaceholder("chat_history"),
             ("human", "{input}"),
         ]
          )
        return self.context
    
