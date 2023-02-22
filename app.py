from summarize import summarize
from uploader_service import upload
from get_articles import get_articles

def main():
    articles = get_articles(number_of_stories=10)
    # For each article, generate summaries of full articles
    summarized_articles = []
    for article in articles:
        summary = summarize(article=article['content'])
        article['summary'] = summary['choices'][0]['text']
        summarized_articles.append(article)

    # Upload the entire article including summaries
    upload(summarized_articles)
    
if __name__ == "__main__":
    main()
    