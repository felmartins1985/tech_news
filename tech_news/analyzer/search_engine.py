from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_tuple = []
    for new in search_news({"title": {"$regex": title, "$options": "i"}}):
        news_tuple.append((new["title"], new["url"]))
    return news_tuple


# Requisito 7
def search_by_date(date):
    try:
        news_tuple = []
        news_by_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        for new in search_news({"timestampt": {{"$eq": news_by_date}}}):
            news_tuple.append((new["title"], new["url"]))
        return news_tuple
    except ValueError:
        raise ValueError("Data inválida")


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
        news_tuple.append((new["title"], new["url"]))
    return news_tuple
