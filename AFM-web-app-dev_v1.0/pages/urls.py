# pages/urls.py

from django.urls import path
from .views import HomePageView, NewsListView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('news/', NewsListView.as_view(), name='news_list'),
]
