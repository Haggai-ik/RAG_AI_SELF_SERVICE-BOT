from langchain.chains import create_history_aware_retriever
from LLM.llm_model import  llm_model


class history_aware_retriever:

    
    def history_aware_retriever(model,db,context_prompt):

        history_aware_retriever = create_history_aware_retriever(
        model, db, context_prompt
        )

        return history_aware_retriever
