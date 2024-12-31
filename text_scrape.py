#!/usr/bin/python3

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
html = Request('https://businessday.ng/category/markets/feed/', headers=headers)
req = urlopen(html)
bs = BeautifulSoup(req, 'xml')
items = bs.select('item')

for item in items:
    title = item.select_one('title').text  # Extract title
    link = item.select_one('link').text  # Extract link
    description_html = item.select_one('description').text.strip()
    description_soup = BeautifulSoup(description_html, 'html.parser').find('img').get('alt')
    #description = description_soup.get_text(separator=' ', strip=True)  # Extract description
    pub_date = item.select_one('pubDate').text  # Extract pubDate
    creator = item.find('dc:creator').text.strip() # creator
    categories = item.select_one('category').text  # Extract all categories

    print(f"Title: {title}")
    print(f"Link: {link}")
    print(f"Description: {description_soup}")
    print(f"Published on: {pub_date}")
#    print(f"Categories: {[category.text for category in categories]}")
    print(f"Author: {creator}")
    print("-" * 40) 
