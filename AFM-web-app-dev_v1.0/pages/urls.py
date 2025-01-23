# pages/urls.py

from django.urls import path
from .views import HomePageView, NewsListView, FinancialMarketView, AboutPageView, SearchRedirectView, StockProfileView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('about/', AboutPageView.as_view(), name='about'),
   # path('financial_market/stock/', FinancialMarketView.as_view(), {'market_type': 'stock'}, name='financial_market_stock'),
    #path('financial_market/crypto/', FinancialMarketView.as_view(), {'market_type': 'crypto'}, name='financial_market_crypto'),
    path('financial-market/<str:market_type>/', FinancialMarketView.as_view(), name='financial_market'),
    path('search/', SearchRedirectView.as_view(), name='search'),
    path('stock_profile/', StockProfileView.as_view(), name='stock_profile')
]
