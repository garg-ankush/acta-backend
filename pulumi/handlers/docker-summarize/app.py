import json
import base64
import os
import requests
from summarize import summarize
from uploader_service import upload
from get_articles import get_articles
from dotenv import load_dotenv

load_dotenv()

def handler(event, context):
    articles = get_articles(number_of_stories=10)
    # For each article, generate summaries of full articles
    summarized_articles = []
    for article in articles:
        content = article['content']

        # Only take 2040 characters to summarize
        if len(content) > 2000:
            content = content[:2000]

        summary = summarize(article=content)
        article['summary'] = summary['choices'][0]['text']
        summarized_articles.append(article)

    # Upload the entire article including summaries
    upload(summarized_articles)

    # After upload completes, send a post content to an api
    for article in articles:
        content = article['content']
        
        # Only take 6000 characters to summarize
        if len(content) > 3000:
            content = content[:3000]

        response = requests.post(
            url=os.getenv("API_TEXT_TO_SPEECH"),
            json={
                "text": content,
                "textId": article['id'],
                "voiceId": "Joanna"
                })
    return {
        "status": 200,
        "description": "Complete."
    }
    