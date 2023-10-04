class Config:
    def __init__(self, openai_api_key="", temperature=0.9, max_token=500):
        self.openai_api_key = openai_api_key
        self.temperature = temperature
        self.max_token = max_token