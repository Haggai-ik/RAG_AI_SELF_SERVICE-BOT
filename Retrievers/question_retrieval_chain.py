from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain


class document_question_chain:
    def __init__(self,model,prompt,retriever):
        self.model =model
        self.prompt =prompt
        self.retriever =retriever
        self.question_answer_chain =None
        self.rag_chain_history = None


    def question_retrieval_chain(self):
        self.question_answer_chain =create_stuff_documents_chain(self.model, self.prompt)
        self.rag_chain_history = create_retrieval_chain(self.retriever, self.question_answer_chain)

        return self.rag_chain_history




