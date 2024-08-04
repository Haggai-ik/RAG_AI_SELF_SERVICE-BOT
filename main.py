import os
from dotenv import load_dotenv
from LLM.llm_embeddings import llm_embeddings
from LLM.llm_model import llm_model
from Data_Loader_Spliter.data_loader_splitter  import ExcelLoader,TextSplitter
from Vector_Database.vector_database import vector_db
from prompts.prompts import system_prompt,chat_history_system_prompt
from prompts.chat_prompt_tempate import chatprompt
from Retrievers.history_aware_retriever import history_aware_retriever
from Retrievers.question_retrieval_chain import document_question_chain
from Chat_History.chat_history  import chat_history_question



def initialize_model_embedding_vector_ragchain():
        Google_api_key =os.getenv('GEMINI_PRO_API_KEY')
        COMPANY_DATASET_PATH = os.getenv('COMPANY_DATASET_PATH')

        llm = llm_model(model_name='gemini-pro',api_key=Google_api_key,temperature=0.5,convert_system_message_to_human=True)
        model = llm.initialize_model()

        embeddings =llm_embeddings(model_emb_name='models/embedding-001',api_key=Google_api_key)
        google_embeddings=embeddings.llm_embedding()

        loader =ExcelLoader(file_path=COMPANY_DATASET_PATH)
        docs = loader.load_excel()
        
        splitter = TextSplitter(docs)
        chunks = splitter.split_text()

        vdb= vector_db(chunks,google_embeddings)
        db =vdb.vector_databse_retriever()

        chatprompting_hist =chatprompt(context_prompt=chat_history_system_prompt)
        chatprompt_hist =chatprompting_hist.use_chat_template()


        history_retriever =history_aware_retriever.history_aware_retriever(model=model,db=db,context_prompt=chatprompt_hist)

        chatprompting =chatprompt(context_prompt=system_prompt)
        chatprompting =chatprompting.use_chat_template()

        document_question  =document_question_chain(model=model,prompt=chatprompting,retriever=history_retriever)
        rag_chain_history =document_question.question_retrieval_chain()


        llm_answer= chat_history_question(session_id='1',rag_chain_history=rag_chain_history)

        conversational_rag_chain =llm_answer.conversational_rag_chain_answer()

        return  llm_answer,conversational_rag_chain


def question_answer(llm_answer, question):
        return llm_answer.question_answer(question)


# llm_answer,conversational_rag_chain = initialize_model_embedding_vector_ragchain()
# question =" hello there"
# print(question_answer(llm_answer, question))
# print(llm_answer.view_chat_history())





