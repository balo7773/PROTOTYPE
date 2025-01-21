# accounts/views.py
# from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, TemplateView
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

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
            # Check for MEDIA_URL and MEDIA_ROOT settings
            if not hasattr(settings, 'MEDIA_URL') or not hasattr(settings, 'MEDIA_ROOT'):
                print("MEDIA_URL or MEDIA_ROOT not set in settings.py")
                messages.error(request, "Error: Missing MEDIA_URL or MEDIA_ROOT settings.")
                return redirect('profile')

            # Update profile picture
            user.profile_picture = profile_picture
            user.save()

            # Print file path for debugging
            print(f"Uploaded image saved to: {user.profile_picture.path}")

            messages.success(request, "Profile picture updated successfully!")
        return redirect('profile')