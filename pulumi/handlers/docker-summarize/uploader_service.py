import os
import time
from pymongo import MongoClient

class Uploader:
    def __init__(self):
        self.mongo_client = MongoClient(os.getenv("MONGODB_URI"))
        self.database = self.mongo_client.get_database('articlesDB')
        self.articles_collection = self.database.get_collection('articlesCollection')

    def upload(self, articles):
        return self.articles_collection.insert_one({
            str(round(time.time())): articles
        })

def upload(articles):
    uploader = Uploader()
    uploader.upload(articles)
    print("Upload complete..")
