#!/usr/bin/python3

from urllib.request import urlopen, Request
import requests
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from datetime import datetime
# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('NEWS_API_KEY')
params = {
            'api_token' : api_key,
            'published_on' : datetime.now().strftime('%Y-%m-%d'),
            'categories' : 'business',
            'locale' : 'us',
            'language' : 'en'
        }

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'} # header
class News_API:

    def __init__ (self, Title='', Author='', Publishers='News_API', Description='', Link='', Date='', Image='', Data=[]):
        self.Title = Title
        self.Author = Author
        self.Publishers = Publishers
        self.Description = Description
        self.Link = Link
        self.Date = Date
        self.Image = Image
        self.Data = Data

    def add_data(self, **kwargs):
        new_data = {
            'Title': kwargs.get('Title', self.Title),
            'Author': kwargs.get('Author', self.Author),
            'Publishers': kwargs.get('Publishers', self.Publishers),
            'Description': kwargs.get('Description', self.Description),
            'Link': kwargs.get('Link', self.Link),
            'Image': kwargs.get('Image', self.Image),
            'Date': kwargs.get('Date', self.Date)
        }
        self.Data.append(new_data)

    def get_data(self):
        return self.Data

class NairaMetrics(News_API):
    def __init__(self, Title='', Author='', Publishers='NairaMetrics', Description='', Link='', Image='', Date=''):
        super().__init__(Title, Author, Publishers, Description, Link, Image, Date)
        # self.Category = Category
        self.Image_path = 'static/images/Nairametrics.jpg'

    def get_market_news(self):
        html = Request('https://nairametrics.com/category/market-news/feed/', headers=headers)
        req = urlopen(html)
        
        bs = BeautifulSoup(req, 'xml')
        items = bs.select('item')

        for item in items:
            Title = item.select_one('title').text  # Extract title
            Link = item.select_one('link').text  # Extract link

            _description_html = item.select_one('description').text
            _description_soup = BeautifulSoup(_description_html, 'html.parser').find('p')
            Description = _description_soup.get_text(separator=' ', strip=True)  # Extract description

            Date = item.select_one('pubDate').text  # Extract pubDate
            Author = item.find('dc:creator').text.strip() # creator
            # Category = item.select_one('category').text  # Extract all categories

            # appends to the list
            self.add_data(Title=Title, Author=Author, Publishers=self.Publishers, Description=Description, Link=Link, Image=self.Image_path, Date=Date)

        return self.get_data()


class ThisDailyLive(News_API):
    def __init__(self, Title='', Author='', Publishers='ThisDailyLive', Description='', Link='', Image='',Date=''):
        super().__init__(Title, Author, Publishers, Description, Link, Image, Date)
        self.Image_path = 'static/images/Thisdailylive.jpg'

    def get_market_news(self):
        html = Request('https://www.thisdaylive.com/index.php/category/business/feed/', headers=headers)
        req = urlopen(html)

        bs = BeautifulSoup(req, 'xml')
        items = bs.select('item')

        for item in items:
            Title = item.select_one('title').text
            Link = item.select_one('link').text
            Description = item.select_one('description').text.strip()
            Date = item.select_one('pubDate').text
            Author = item.find('dc:creator').text.strip()

            self.add_data(Title=Title, Author=Author, Publishers=self.Publishers, Description=Description, Link=Link, Image=self.Image_path,Date=Date)

        return self.get_data()

class BusinessDay(News_API):
    def __init__(self, Title='', Author='', Publishers='BusinessDay', Description='', Link='', Date=''):
        super().__init__(Title, Author, Publishers, Description, Link, Date)
        self.Image_path = 'static/images/Businessday.png'

    def get_market_news(self):
        html = Request('https://businessday.ng/category/markets/feed/', headers=headers)
        req = urlopen(html)

        bs = BeautifulSoup(req, 'xml')
        items = bs.select('item')

        for item in items:
            Title = item.select_one('title').text
            Link = item.select_one('link').text
            _description_html = item.select_one('description').text
            _description_soup = BeautifulSoup(_description_html, 'html.parser').find('img').get('alt')
            Description = _description_soup
            Date = item.select_one('pubDate').text
            Author = item.find('dc:creator').text.strip()

            self.add_data(Title=Title, Author=Author, Publishers=self.Publishers, Description=Description, Link=Link, Image=self.Image_path, Date=Date)

        return self.get_data()
            
class USA_NEWS(News_API):


    def __init__(self, Title='', Author='',Publishers='', Description='', Link='', Image ='', Date=''):
        super().__init__(Title, Author, Publishers, Description, Link, Image, Date)

    def get_market_news(self):
        response = requests.get(f'https://api.thenewsapi.com/v1/news/top', params=params)
        response_data = response.json().get('data', {})
        
        for item in response_data:
            Title = item.get('title')
            Link = item.get('url')
            Description = item.get('description')
            Date = datetime.strptime(item.get('published_at'), '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d')
            Publishers = item.get('source')
            Image = item.get('image_url')

            self.add_data(Title=Title, Publishers=Publishers, Description=Description, Link=Link, Image=Image, Date=Date)

        return self.get_data()
    
    
    
    
    
    
""""""