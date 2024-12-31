#!/usr/bin/python3:wq

from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'} # header
class News_API:

    def __init__ (self, Title='', Author='', Publishers='News_API', Description='', Link='', Date='', Data=[]):
        self.Title = Title
        self.Author = Author
        self.Publishers = Publishers
        self.Description = Description
        self.Link = Link
        self.Date = Date
        self.Data = Data

    def add_data(self):
        new_data = {
                        'Title' : self.Title,
                        'Author' : self.Author,
                        'Publishers' : self.Publishers,
                        'Description' : self.Description,
                        'Link' : self.Link,
                        'Date' : self.Date 
                    }
        self.Data.append(new_data)

    def get_data(self):
        return self.Data

class NairaMetrics(News_API):
    def __init__(self, Title='', Author='', Publishers='NairaMetrics', Description='', Link='', Date=''):
        super().__init__(Title, Author, Publishers, Description, Link, Date)
        # self.Category = Category

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
            self.add_data(Title=Title, Author=Author, Publishers=self.Publishers, Description=Description, Link=Link, Date=Date)

        return self.get_data()


class ThisDailyLive(News_API):
    def __init__(self, Title='', Author='', Publishers='ThisDailyLive', Description='', Link='', Date=''):
        super().__init__(Title, Author, Publishers, Description, Link, Date)

    def get_market_news(self):
        html = Request('/https://www.thisdaylive.com/index.php/category/business/feed/', headers=headers)
        req = urlopen(html)

        bs = BeautifulSoup(req, 'xml')
        items = bs.select('item')

        for item in items:
            Title = item.select_one('title').text
            Link = item.select_one('link').text
            Description = item.select_one('description').text.strip()
            Date = item.select_one('pubDate').text
            Author = item.find('dc:creator').text.strip()

            self.add_data(Title=Title, Author=Author, Publishers=self.Publishers, Description=Description, Link=Link, Date=Date)

        return self.get_data()

class BusinessDay(News_API):
    def __init__(self, Title='', Author='', Publishers='BusinessDay', Description='', Link='', Date=''):
        super().__init__(Title, Author, Publishers, Description, Link, Date)

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

            self.add_data(Title=Title, Author=Author, Publishers=self.Publishers, Description=Description, Link=Link, Date=Date)

        return self.get_data()
            
