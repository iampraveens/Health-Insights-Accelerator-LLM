import logging
from langchain.chains import RetrievalQAWithSourcesChain

class Chain:
    def __init__(self, llm, retriever):
        self.llm = llm
        self.retriever = retriever
        
    def answer_question(self, query):
        try:
            chain = RetrievalQAWithSourcesChain.from_llm(llm=self.llm, retriever=self.retriever.as_retriever())
            result = chain({"question": query}, return_only_outputs=True)
            return result["answer"]
        except Exception as e:
            logging.error(f"Error answering question")
            raise e