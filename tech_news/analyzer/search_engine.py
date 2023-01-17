from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news_tuple = []
    for new in search_news({"title": {"$regex": title, "$options": "i"}}):
        news_tuple.append((new["title"], new["url"]))
    return news_tuple


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    news_tuple = []
    for new in search_news({"tags": {"$regex": tag, "$options": "i"}}):
        news_tuple.append((new["title"], new["url"]))
    return news_tuple


# Requisito 9
def search_by_category(category):
    news_tuple = []
    for new in search_news(
        {"category": {"$regex": category, "$options": "i"}}
    ):
        news_tuple.append(new["title"], new["url"])
    return news_tuple
