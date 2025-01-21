# accounts/urls.py
import os
from django.urls import path
from .views import SignupPageView, CustomLoginView, ProfilePageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("profile/", ProfilePageView.as_view(), name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)