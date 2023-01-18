from tech_news.database import find_news
from operator import itemgetter
from collections import Counter


# Requisito 10
def top_5_news():
    comments = []
    for new in find_news():
        comments.append(new)
    title_sorted = sorted(comments, key=itemgetter("title"))
    comments_sorted = sorted(
        title_sorted, key=itemgetter("comments_count"), reverse=True
    )
    return comments_sorted[:5]


# Requisito 11
def top_5_categories():
    categories = []
    for new in find_news():
        categories.append(new["category"])
    categories_count = []
    for name, count in Counter(sorted(categories)).most_common(5):
        categories_count.append(name)
    return categories_count


print(top_5_news())
