import requests
import json
from config import TWITTER_API_KEY, NEWS_API_KEY

# X (formerly Twitter) API Fetcher
def fetch_x_data(query):
    url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&tweet.fields=created_at,text"
    headers = {"Authorization": f"Bearer {TWITTER_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()

# News API Fetcher
def fetch_news_data(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    return response.json()
