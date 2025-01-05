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

    template_name = "home.html"
    context_object_name = "top_news"

    def get_queryset(self):
        nairametrics = NairaMetrics().get_market_news()
        this_daily_live = ThisDailyLive().get_market_news()
        businessday = BusinessDay().get_market_news()
        usa_news = USA_NEWS().get_market_news()
        List_of_news = nairametrics + this_daily_live + businessday + usa_news
        
        NEWS = []
        today = datetime.now().date()
        
        for all_news in List_of_news:
            news_date = all_news.get('Date')
            if news_date:
                try:
                    # Try parsing the date string using dateutil
                    if isinstance(news_date, str):
                        parsed_date = parser.parse(news_date).date()
                    else:
                        parsed_date = news_date.date()
                    
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
