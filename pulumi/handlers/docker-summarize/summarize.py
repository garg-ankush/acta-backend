import os
import openai

# Constants
MODEL_NAME = "text-davinci-003"
TEMPERATURE = 0.7 # Higher values make output more random
MAX_TOKENS = 60
TOP_P = 1 # Higher values make output more random
FREQUENCY_PENALTY = 0
PRESENCE_PENALTY = 1


class Summarizer:
    def __init__(self):
        self.model_name = MODEL_NAME
        self.openAI = openai 
        self.temperature = TEMPERATURE
        self.max_tokens = MAX_TOKENS 
        self.top_p = TOP_P
        self.frequency_penalty = FREQUENCY_PENALTY
        self.presence_penalty = PRESENCE_PENALTY
    
    
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