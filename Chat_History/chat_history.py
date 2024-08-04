from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

class chat_history_question:
    def __init__(self,session_id,rag_chain_history):
        self.store ={}
        self.session_id =session_id
        self.rag_chain_history =rag_chain_history

    def get_session_history(self) -> BaseChatMessageHistory:
        if self.session_id not in self.store:
            self.store[self.session_id]= ChatMessageHistory()

        return self.store[self.session_id]  
             
    

    def conversational_rag_chain_answer(self):
        self.conversational_rag_chain = RunnableWithMessageHistory(
         self.rag_chain_history,
          self.get_session_history,
          input_messages_key="input",
          history_messages_key="chat_history",
        output_messages_key="answer",
          )
        
        return self.conversational_rag_chain
        
         
         


    def  question_answer(self,question):
    #     results = []
    #     for result in self.conversational_rag_chain.stream(
    #          {"input": question},
    #           config={
    #         "configurable": {"session_id": self.session_id}
    #           }
    #           ):
            
    #      results.append(result)

    # # Assuming you want to return the "answer" from the first result
    #     if results:
    #         return results[0]["answer"]
    #     else:
    #             return None
    #     # results =[]
        result = self.conversational_rag_chain.invoke(
          {"input": question},
        config={
        "configurable": {"session_id": self.session_id}
          },
        )["answer"]

        return result
    
    def view_chat_history(self):
        return self.store

