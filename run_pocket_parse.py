from pocket_article import PocketArticle

articles = PocketArticle.get_articles()

for article in articles:
    with open(article.id, 'w') as f:
        f.write(article.text)