# pages/views.py

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .dynamic_api import NairaMetrics, ThisDailyLive, BusinessDay, USA_NEWS
from datetime import datetime, date
from dateutil import parser


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

class FinancialMarketView(TemplateView):
    template_name = 'financial_market.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        market = kwargs.get('market_type')  # Ensure `market_type` is correctly accessed

        # Set widget configuration based on the market type
        if market == 'stock':
            context['widget_data'] = {
                "width": "100%",
                "height": 550,
                "defaultColumn": "overview",
                "defaultScreen": "most_capitalized",
                "market": "america",  # Required for stocks
                "colorTheme": "light",  # Matches your desired widget
                "showToolbar": True,
                "isTransparent": True,
                "locale": "en",
            }
        elif market == 'crypto':
            context['widget_data'] = {
                "width": "100%",
                "height": 550,
                "defaultColumn": "overview",
                "screener_type": "crypto_mkt",  # Required for crypto
                "displayCurrency": "USD",  # Specific to crypto
                "colorTheme": "light",
                "isTransparent": True,
                "locale": "en",
            }
        else:
            # Handle invalid market types
            context['widget_data'] = None

        return context


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
    login_url = reverse_lazy("login")  # Redirect if not logged in
