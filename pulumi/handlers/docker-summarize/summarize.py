import os
import openai

# Constants
MODEL_NAME = "gpt-3.5-turbo"

class Summarizer:
    def __init__(self):
        self.model_name = MODEL_NAME
        self.openAI = openai
    
    def setup(self):
        self.openAI.api_key = os.getenv("OPENAI_API_KEY")

    def summarize(self, text: str):
        return self.openAI.ChatCompletion.create(
            model=self.model_name,
            messages=[{
                "role": "user",
                "content": f"Summarize this in 100 words: {text}"
            }]
        )
        

def summarize(article):
    summarizer = Summarizer()
    summarizer.setup()
    return summarizer.summarize(article)