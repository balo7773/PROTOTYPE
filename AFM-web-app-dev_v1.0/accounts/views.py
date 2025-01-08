# accounts/views.py
# from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomLoginForm

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = "registration/login.html"
