FROM python:3.10-slim-buster
RUN apt-get update
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --index-url=https://pypi.org/simple/ --timeout=60
ENTRYPOINT ["nohup", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]