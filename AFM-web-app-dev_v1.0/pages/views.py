# pages/views.py

from django.shortcuts import render

"""
from django.http import HttpResponse
def home_page_view(request):
return HttpResponse("Hello, World!")
"""
def home_page_view(request):
    return render(request, "home.html")

"""
from django.views.generic import TemplateView
class HomePageView(TemplateView):
template_name = "home.html
"""