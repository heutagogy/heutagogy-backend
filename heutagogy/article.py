from heutagogy.persistence import db, Bookmark

from newspaper import Article


def fetch_article(id, url):
    article = Article(url, keep_article_html=True)
    article.download()
    article.parse()

    bookmark = Bookmark.query.get(id)
    if bookmark.title == bookmark.url and article.title != '':
        # title was not set
        bookmark.title = article.title

    bookmark.content_html = article.article_html
    bookmark.content_text = article.text

    db.session.commit()
