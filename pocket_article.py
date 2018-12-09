
import pocket_client
from newspaper import Article


class PocketArticle:
    def __init__(self, article_id, title, url, text):
        self.id = article_id
        self.title = title
        self.url = url
        self.text = text

    """
    Fetches all unread pocket articles, parses text and forms a list of PocketArticle's.
    
    Returns:
        List(PocketArticle) -- A list of PocketArticle's
    """
    @staticmethod
    def get_articles():
        return [PocketArticle(
            article['item_id'],
            article['given_title'],
            article['given_url'],
            PocketArticle.__retrieve_article_text(article['given_url']))
            for article in pocket_client.fetch_unread_articles().json()['list'].values()]

    @staticmethod
    def __retrieve_article_text(url):
        article = Article(url)
        article.download()
        article.parse()
        return article.text
