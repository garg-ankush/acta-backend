import os
from datetime import datetime, timedelta
import newspaper
import uuid
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

# Init
newsAPI_client = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))

TOPIC="climate"
DATE_FORMAT = "%Y-%m-%d"
NUMBER_OF_DAYS_FOR_NEWS = 3

END_DATE = datetime.today()
START_DATE = datetime.today() - timedelta(NUMBER_OF_DAYS_FOR_NEWS)

def get_N_headline_stories(number_of_stories=10):
    return newsAPI_client.get_everything(
        q=TOPIC,
        language='en',
        from_param=START_DATE.strftime(DATE_FORMAT),
        to=END_DATE.strftime(DATE_FORMAT),
        sort_by='popularity',
        page=1,
        page_size=number_of_stories
        )

def get_full_article(headline: dict):   
    headline_url = headline.get('url')
    article = newspaper.Article(url=headline_url, language='en')
    article.download()
    article.parse()
    return article.text

def get_articles(number_of_stories=10):
    full_stories = []
    headline_stories = get_N_headline_stories(number_of_stories=number_of_stories)
    for headline_story in headline_stories['articles']:
        full_article = get_full_article(headline_story)
        complete_story = {
            "author": headline_story['author'],
            "title": headline_story['title'],
            "url": headline_story['url'],
            "image": headline_story['urlToImage'],
            "published_at": headline_story['publishedAt'],
            "content": full_article,
            "id": str(uuid.uuid1())
        }
        full_stories.append(complete_story)
    return full_stories


