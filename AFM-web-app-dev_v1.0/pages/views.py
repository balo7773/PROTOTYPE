# pages/views.py

from django.shortcuts import render
from django.views.generic import ListView
from .dynamic_api import NairaMetrics, ThisDailyLive, BusinessDay, USA_NEWS
from datetime import datetime, date
from dateutil import parser

"""
from django.http import HttpResponse
def home_page_view(request):
return HttpResponse("Hello, World!")
def home_page_view(request):
    return render(request, "home.html")

"""

class HomePageView(ListView):
    '''
    Inherits from django ListView,
    to display home page.
    '''

    template_name = "home.html"
    context_object_name = "top_news" # News identifier in django template.

    def get_queryset(self):
        '''
        Django named function to return data to views
        
        Return:
        returns data to be used on home template
        '''
        nairametrics = NairaMetrics().get_market_news()
        this_daily_live = ThisDailyLive().get_market_news()
        businessday = BusinessDay().get_market_news()
        usa_news = USA_NEWS().get_market_news()
        List_of_news = nairametrics + this_daily_live + businessday + usa_news
        
        NEWS = [] # Storing top news data.
        today = datetime.now().date()
        
        for all_news in List_of_news:
            # Loop through list of news,
            # to get only up to date news.
            news_date = all_news.get('Date') # Get all news date.
            if news_date:
                try:
                    #  Parsing the date string using dateutil.
                    if isinstance(news_date, str):
                        parsed_date = parser.parse(news_date).date()
                    else:
                        parsed_date = news_date.date()

                    # If the date is today, append news.
                    if parsed_date == today:
                        NEWS.append(all_news)
                        print(f"Added news item: {all_news.get('Title')}")  # Debug print
                        
                        if len(NEWS) == 4:
                            break
                except (ValueError, AttributeError) as e:
                    print(f"Error parsing date: {news_date}, Error: {e}")
                    continue
        
        print(f"Final number of news items: {len(NEWS)}")
        return NEWS


class NewsListView(ListView):
    '''
    Class-based view to display paginated news from various sources.
    '''
    template_name = "news.html"
    context_object_name = "news"  # Variable name in the template
    paginate_by = 12  # Number of items per page

    def get_queryset(self):
        '''
        Override the method to dynamically fetch and filter news.
        
        Return:
        - List of today's news items from multiple sources.
        '''
        # Fetch news from different sources
        nairametrics = NairaMetrics().get_market_news()
        this_daily_live = ThisDailyLive().get_market_news()
        businessday = BusinessDay().get_market_news()
        usa_news = USA_NEWS().get_market_news()
        List_of_news = nairametrics + this_daily_live + businessday + usa_news

        NEWS = []  # List to store today's news

        for all_news in List_of_news:
            # Loop through all news items to filter by today's date
            news_date = all_news.get('Date')  # Get the date of the news item
            if news_date:
                try:
                    # Parse the date string using dateutil
                    if isinstance(news_date, str):
                        parsed_date = parser.parse(news_date).date()
                    else:
                        parsed_date = news_date.date()

                    # Append the news if the date is today
                    #if parsed_date == today:
                    NEWS.append(all_news)

                except (ValueError, AttributeError) as e:
                    print(f"Error parsing date: {news_date}, Error: {e}")
                    continue

        return NEWS

"""from django.core.paginator import Paginator
from django.shortcuts import render
from .models import News  # Replace with your model

def news_list(request):
    news = News.objects.all()
    paginator = Paginator(news, 12)  # 12 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})
"""
