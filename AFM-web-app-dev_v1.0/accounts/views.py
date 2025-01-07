# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# Sign Up View
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save the user
            form.save()
            # Redirect to login page after successful sign-up
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')  # Redirect to login page after successful sign-up
        else:
            # Form is not valid, show form errors
            messages.error(request, "There was an error with the form. Please try again.")
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


# Login View
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']

            # Check if the login is using username or email
            try:
                user = User.objects.get(username=username_or_email)
            except User.DoesNotExist:
                user = User.objects.filter(email=username_or_email).first()

            if user and user.check_password(password):
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('home')  # Redirect to homepage or dashboard after successful login
            else:
                messages.error(request, "Invalid credentials, please try again.")

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
