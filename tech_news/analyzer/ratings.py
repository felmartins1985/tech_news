from tech_news.database import find_news

from collections import Counter


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""


# Requisito 11
def top_5_categories():
    categories = []
    for new in find_news():
        categories.append(new["category"])
    categories_count = []
    for name, _ in Counter(categories).most_common(5):
        categories_count.append(name)
    return categories_count


print(top_5_categories())
