from langchain_google_genai import GoogleGenerativeAIEmbeddings


class llm_embeddings:

    def __init__(self, model_emb_name, api_key):
        self.model_emb_name  =model_emb_name
        self.api_key  =api_key
        self.embeddings =None

    def llm_embedding(self):
        self.embeddings = GoogleGenerativeAIEmbeddings(model=self.model_emb_name,
                    google_api_key=self.api_key)
        return self.embeddings
    
    