import os
import streamlit as st 
import requests
from io import BytesIO
from PIL import Image
from langchain.llms import OpenAI

from config import Config
from data_ingest import DataIngest
from vector_store import VectorStore
from chain import Chain

url = "https://cdn-icons-png.flaticon.com/512/4149/4149701.png"
response = requests.get(url)
image = Image.open(BytesIO(response.content))
page_title = 'Insights Accelerator'
page_icon = image
layout = 'centered'

st.set_page_config(page_title=page_title,
                   page_icon=page_icon,
                   layout=layout
                   )

hide_style = '''
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            <style>
            
            '''
header_style = '''
             <style>
             .navbar {
                 position: fixed;
                 top: 0;
                 left: 0;
                 width: 100%;
                 z-index: 1;
                 display: flex;
                 justify-content: center;
                 align-items: center;
                 height: 80px;
                 background-color: #626567;
                 box-sizing: border-box;
             }
             
             .navbar-brand {
                 color: white !important;
                 font-size: 23px;
                 text-decoration: none;
                 margin-right: auto;
                 margin-left: 50px;
             }
             
             .navbar-brand img {
                margin-bottom: 6px;
                margin-right: 1px;
                width: 40px;
                height: 40px;
                justify-content: center;
            }
            
            /* Add the following CSS to change the color of the text */
            .navbar-brand span {
                color: #EF6E04;
                justify-content: center;
            }
            
             </style>
             
             <nav class="navbar">
                 <div class="navbar-brand">
                <img src="https://cdn-icons-png.flaticon.com/512/4149/4149701.png" alt="Logo">
                    Insights Accelerator - Research Tool
                 </div>
             </nav>
               '''
st.markdown(hide_style, unsafe_allow_html=True)
st.markdown(header_style, unsafe_allow_html=True)

# Load configuration
config = Config()

openai_api_key = st.sidebar.text_input("Enter your OpenAPI Key:", type="password", key="api_key")
config.openai_api_key = openai_api_key

if config.openai_api_key:
    llm = OpenAI(openai_api_key=config.openai_api_key)

urls = []
for i in range(2):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)
    
query = st.chat_input(placeholder="Ask me something")

if query:
    
    data_loader = DataIngest(urls)
    documents = data_loader.ingest_data()
    
    vector_store = VectorStore(openai_api_key=config.openai_api_key, 
                            documents=documents)
    
    vectorstore_retreiver = vector_store.create_store()
    chain = Chain(llm=llm, retriever=vectorstore_retreiver)
    answer = chain.answer_question(query=query) 
    
    st.header("Response")
    st.write(answer)