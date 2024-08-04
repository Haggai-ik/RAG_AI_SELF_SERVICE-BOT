from langchain.document_loaders import UnstructuredExcelLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


class TextSplitter:
    def __init__(self, docs, chunk_size=1000, chunk_overlap=200, separators=["\n\n\n", "\n\n", "\n"]):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.docs = docs
        self.separators = separators

    def split_text(self):
        context = "\n\n".join(str(doc.page_content).replace('\r\n', '\n').strip() for doc in self.docs if doc.page_content)
        
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=self.separators
        )
        
        chunks = text_splitter.split_text(context)
        return chunks

class ExcelLoader:
    def __init__(self, file_path, mode='elements'):
        self.filepath = file_path
        self.mode = mode

    def load_excel(self):
        loader = UnstructuredExcelLoader(file_path=self.filepath, mode=self.mode)
        docs = loader.load()
        return docs



    


