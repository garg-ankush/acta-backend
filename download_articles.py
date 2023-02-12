import os
import time
from typing import List
from datetime import datetime, timedelta
import newspaper
import uuid
import json
from dotenv import load_dotenv
from newsapi import NewsApiClient
from pymongo import MongoClient

load_dotenv()

# Download latest articles of the week
# For those articles, download full text
# For the full text, generate summaries --> on GPUs
# Store the full text, article title, published date, article url and summary in the mongo database

# Init
newsAPI_client = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))
mongo_client = MongoClient(os.getenv("MONGODB_URI"))

TOPIC="climate"
DATE_FORMAT = "%Y-%m-%d"
NUMBER_OF_DAYS_FOR_NEWS = 3

END_DATE = datetime.today()
START_DATE = datetime.today() - timedelta(NUMBER_OF_DAYS_FOR_NEWS)

def get_top_N_headlines(number_of_headlines=10):
    return newsAPI_client.get_everything(
        q=TOPIC,
        language='en',
        from_param=START_DATE.strftime(DATE_FORMAT),
        to=END_DATE.strftime(DATE_FORMAT),
        sort_by='popularity',
        page=1,
        page_size=number_of_headlines
        )

def upload_headlines(headlines: List):
    complete_stories = {}
    timestamp = round(time.time())

    for index, headline in enumerate(headlines):        
        headline_url = headline.get('url')
        article = newspaper.article = newspaper.Article(url=headline_url, language='en')
        article.download()
        article.parse()

        headline_content = article.text

        headlines[index]['content'] = headline_content
        headlines[index]['id'] = str(uuid.uuid1())

    complete_stories[str(timestamp)] = headlines

    database = mongo_client.get_database('articlesDB')
    articles_collection = database.get_collection('articlesCollection')

    print(complete_stories)

    print("uploading....")
    articles_collection.insert_one(complete_stories)
    print("upload complete.")


# def get_article_text(headlines):
#     for headline in headlines:
#         # Use the library to get text from a URL
#         pass

# def summarize(headlines):
#     summaries = [] 
#     for headline in headlines:
#         summarized_text = summarize(headline)
#         summaries.append(summarized_text)

#     return summaries

def main():
    headlines = get_top_N_headlines(number_of_headlines=10)
    upload_headlines(headlines.get('articles'))


    
    # summaries = summarize(headlines=headlines)

if __name__ == "__main__":
    main()