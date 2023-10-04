import logging
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class DataIngest:
    def __init__(self, urls):
        self.urls = urls
        
    def ingest_data(self):
        try:
            loader = UnstructuredURLLoader(self.urls)
            data = loader.load()
            return data
        except Exception as e:
            logging.error(f"Error loading data")
            raise e
    
    def split_data(self):
        try:
            splitter = RecursiveCharacterTextSplitter(
                separators=["\n\n", "\n", ".", " "],
                chunk_size=1000,
                chunk_overlap=200
            )
            data = self.ingest_data()
            documents = splitter.split_text(data)
            return documents
        except Exception as e:
            logging.error(f"Error splitting data")
            raise e
        