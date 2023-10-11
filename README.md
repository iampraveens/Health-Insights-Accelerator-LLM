# Health Insights Accelerator - Research Tool <img src="https://cdn-icons-png.flaticon.com/512/10394/10394376.png" alt="Health Insights Accelerator - Research Tool" width="50" height="50">

## Application
Deployed the model on streamlit cloud(temp) [Streamlit App](https://health-insights-accelerator-tool.streamlit.app/)

**Note:- Please use less worded article URLs, not to get an maximum token error**


## Table of Contents
- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
- [Run AI](#run-ai)
- [Usage](#usage)
- [Customization](#customization)
- [Dockerized Web App](#dockerized-web-app)
- [License](#license)

## About
Health Insights Accelerator is a research tool powered by GPT-3 and designed to assist in processing and analyzing health-related documents. This tool allows users to ingest data from URLs, create a vector store for efficient retrieval, and ask questions to extract insights from the processed data.

## Features

- **Data Ingestion:** Easily ingest data from one or more URLs for analysis.
- **Vector Store Creation:** Create a vector store for efficient data retrieval using OpenAI's GPT-3 embeddings and FAISS indexing.
- **Question Answering:** Ask questions related to the ingested data and receive informative answers.

## Getting Started
To get started with this project, you'll need Python and a few libraries installed. Follow these steps:

```bash
git clone https://github.com/iampraveens/Health-Insights-Accelerator-LLM.git
```
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Run AI App

```bash
streamlit run app.py
```

## Usage
- Set up your OpenAI API Key: Enter your API Key in the provided text input on the sidebar.
- In the sidebar, provide URLs of the articles you want to analyze and click the "Process URLs" button. This will ingest the data, create a vector store, and store it as `vector_store.pkl`.
- Enter your research questions in the "Question" text input and enter to retrieve answers.

## Customization
- You can customize the tool's behavior by modifying the `config.py` file to adjust parameters like temperature and token limit.
- For more advanced customizations, you can explore and modify the code in the `data_ingest.py`, `vector_store.py`, and `chain.py` files to tailor the tool to your specific research needs.

## License 
This project is licensed under the MIT License - see the [License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for details.
