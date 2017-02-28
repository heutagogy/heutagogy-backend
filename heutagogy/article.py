from heutagogy.persistence import db, Bookmark

from newspaper import Article


def fetch_article(id, url):
    """Fetch URL and try to parse its title."""
    article = Article(url)
    article.download()
    article.parse()

    bookmark = Bookmark.query.get(id)
    bookmark.title = article.title

    db.session.commit()
