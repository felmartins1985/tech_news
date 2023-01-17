import requests
import time
from parsel import Selector
from tech_news.database import create_news

# Requisito 1


def fetch(url):
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        time.sleep(1)
        response.raise_for_status()
    except (requests.Timeout, requests.HTTPError):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    links_url = selector.css(".cs-overlay-link::attr(href)").getall()
    return links_url


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_link = selector.css(".next::attr(href)").get()
    return next_link


# Requisito 4
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re

    clean = re.compile("<.*?>")
    return re.sub(clean, "", text)


def scrape_news(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = len(selector.css("comment-list li").getall()) or 0
    summary = remove_html_tags(selector.css(".entry-content p").get())
    tags = selector.css(".post-tags li a::text").getall()
    category = selector.css(".meta-category .label::text").get()

    if not title or not summary:
        return None

    return {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary.strip(),
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    URL = "https://blog.betrybe.com/"
    news = []
    while len(news) <= amount:
        site = fetch(URL)
        news.extend(scrape_updates(site))
        URL = scrape_next_page_link(site)
    tech_news = []
    for new in news[:amount]:
        tech_news.append(scrape_news(fetch(new)))
    create_news(tech_news)
    return tech_news
