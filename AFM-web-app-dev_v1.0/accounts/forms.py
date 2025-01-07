from django import forms
from .models import CustomUser  # Import CustomUser model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    # Age field choices
    age_choices = [
        ('0-18', '0-18'), 
        ('18-35', '18-35'),
        ('36-50', '36-50'),
        ('51-65', '51-65'),
        ('65+', '65+')
    ]
    age = forms.ChoiceField(choices=age_choices, required=True, label="Select Age Group")
    fullname = forms.CharField(max_length=255, required=True, label="Full Name")

    class Meta:
        model = CustomUser  # Use CustomUser here, not User
        fields = ['username', 'email', 'password1', 'password2', 'age', 'fullname']    

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Check if username is less than 4 characters
        if len(username) < 4:
            raise forms.ValidationError("Username must be at least 4 characters long.")

        return username

class LoginForm(AuthenticationForm):
    username_or_email = forms.CharField(label="Username or Email", max_length=254)

    class Meta:
        model = CustomUser  # Use CustomUser here, not User
        fields = ['username_or_email', 'password']

    def clean_username_or_email(self):
        username_or_email = self.cleaned_data['username_or_email']

        # Check if the input is an email
        try:
            validate_email(username_or_email)
            user = CustomUser.objects.filter(email=username_or_email).first()  # Use CustomUser
            if not user:
                raise ValidationError("No user found with this email address.")
        except ValidationError:
            # If it's not a valid email, treat it as a username
            user = CustomUser.objects.filter(username=username_or_email).first()  # Use CustomUser
            if not user:
                raise ValidationError("No user found with this username.")

        return username_or_email
