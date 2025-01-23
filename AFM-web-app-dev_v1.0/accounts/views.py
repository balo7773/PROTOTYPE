# accounts/views.py
# from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, TemplateView, LogoutView
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = "registration/login.html"

class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
    login_url = reverse_lazy("login")

    def post(self, request, *args, **kwargs):
        user = request.user
        profile_picture = request.FILES.get('profile_picture')

        if profile_picture:
            # Debug prints
            print(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")
            print(f"MEDIA_URL: {settings.MEDIA_URL}")
            
            user.profile_picture = profile_picture
            user.save()
            
            # Debug prints
            print(f"Profile picture URL: {user.profile_picture.url}")
            print(f"Profile picture path: {user.profile_picture.path}")
            
            messages.success(request, "Profile picture updated successfully!")
        return redirect('profile')
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")  # Redirect to login page after logout
    http_method_names = ['get', 'post']
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out successfully.")
        return super().dispatch(request, *args, **kwargs)