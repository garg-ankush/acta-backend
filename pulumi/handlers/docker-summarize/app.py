import json
import base64
from summarize import summarize
from uploader_service import upload
from get_articles import get_articles

def handler(event, context):
    # body = event.get('body')
    # if body is None or body == "":
    #     return "Body is empty. Expected JSON object.", 422

    # body = json.loads(base64.b64decode(body))

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

    # Emit a message that the lambda finished it's job
    

    return {
        "status": 200,
        "description": "Complete."
    }
    