import json
import base64
import os
import requests
from summarize import summarize
from uploader_service import upload
from get_articles import get_articles
from dotenv import load_dotenv

load_dotenv()

# Constants
MAX_LENGTH_FOR_ARTICLE_SUMMARIES = 2000
MAX_LENGTH_FOR_ARTICLE_AUDIO = 3000
VOICE_ASSISTANT_NAME = "Joanna"

def handler(event, context):
   MAX_NUMBER_OF_STORIES = os.getenv("NUMBER_OF_STORIES", 10)
   body = event.get('body')
   body = json.loads(base64.b64decode(body))

   topic = body.get("topic", None)
   if topic is None:
    # By default, get climate stories
    topic = "climate"

    # Download the top N articles
    articles = get_articles(topic=topic, number_of_stories=MAX_NUMBER_OF_STORIES)

    # For each article, generate summaries
    summarized_articles = []
    for article in articles:
        content = article['content']

        # Only take 2040 characters to summarize
        # Summarizer model restriction
        if len(content) > MAX_LENGTH_FOR_ARTICLE_SUMMARIES:
            content = content[:MAX_LENGTH_FOR_ARTICLE_SUMMARIES]

        summary = summarize(article=content)
        article['summary'] = summary['choices'][0]['text']
        summarized_articles.append(article)

    # Upload the entire article including summaries
    upload(summarized_articles)

    # After upload completes, send a post content to an api
    for article in articles:
        content = article['content']
        
        # Only take 3000 characters to summarize
        # Amazon Restriction
        if len(content) > MAX_LENGTH_FOR_ARTICLE_AUDIO:
            content = content[:MAX_LENGTH_FOR_ARTICLE_AUDIO]

        response = requests.post(
            url=os.getenv("API_TEXT_TO_SPEECH"),
            json={
                "text": content,
                "textId": article['id'],
                "voiceId": VOICE_ASSISTANT_NAME
                })
    return {
        "status": 200,
        "description": "Complete."
    }
    