import logging
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

class VectorStore:
    def __init__(self, openai_api_key, documents):
        self.openai_api_key = openai_api_key
        self.documents = documents
        
    def create_store(self):
        try:
            embeddings = OpenAIEmbeddings(openai_api_key=self.openai_api_key)
            vectore_store = FAISS.from_documents(documents=self.documents, embedding=embeddings)
            return vectore_store
        except Exception as e:
            logging.error(f"Error creating vector store")
            raise e
            
# class VectorRetreive:
#     def __init__(self, openai_api_key, file_path): 
#         self.openai_api_key = openai_api_key
#         self.file_path = file_path    
#     def load_store(self):
#         try:
#             with open(self.file_path, "rb") as file:
#                 vectore_store = pickle.load(file)
#                 return vectore_store
#         except Exception as e:
#             logging.error(f"Error loading vector store")
#             raise e
            