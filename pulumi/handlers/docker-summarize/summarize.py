import os
import openai

class Summarizer:
    def __init__(self):
        self.model_name = "text-babbage-001"
        self.openAI = openai 
        self.temperature = 0.7
        self.max_tokens=60
        self.top_p=1
        self.frequency_penalty=0
        self.presence_penalty=1
    
    
    def setup(self):
        self.openAI.api_key = os.getenv("OPENAI_API_KEY")

    def summarize(self, text: str):
        return self.openAI.Completion.create(
            model=self.model_name,
            prompt=text,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty
        )
        

def summarize(article):
    summarizer = Summarizer()
    summarizer.setup()
    return summarizer.summarize(article)