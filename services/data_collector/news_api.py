import requests
from bs4 import BeautifulSoup

class NewsScraper:
    @staticmethod
    def fetch_rss_news(rss_urls: list):
        articles = []
        for url in rss_urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "xml")
            articles.extend([item.find("title").text for item in soup.find_all("item")])
        return articles
