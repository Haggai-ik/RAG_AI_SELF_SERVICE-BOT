from langchain_chroma import Chroma


class vector_db:

    def __init__(self,text,embeddings,doc_number =5):
        self.text=text
        self.embeddings=embeddings
        self.doc_number =doc_number


    def vector_databse_retriever(self):
        
        db = Chroma.from_texts(self.text, self.embeddings).as_retriever(search_kwargs={"k":self.doc_number})

        return db