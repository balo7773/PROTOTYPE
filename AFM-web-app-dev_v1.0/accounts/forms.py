# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate


class CustomUserCreationForm(UserCreationForm):

    # Add to your CustomUserCreationForm class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Full Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['age'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Age'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})


    full_name = forms.CharField(max_length=70, label="Full Name")
    age = forms.IntegerField(label="Age", min_value=0)
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = get_user_model()
        fields = (
            "full_name",
            "email",
            "age",
            "password1",
            "password2",
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2


class CustomUserChangeForm(UserChangeForm):
    full_name = forms.CharField(max_length=70, label="Full Name")
    age = forms.IntegerField(label="Age", min_value=0)

    class Meta:
        model = get_user_model()
        fields = (
            "full_name",
            "email",
            "age",
        )


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email',
        }),
        label="Email",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        }),
        label="Password",
    )

    def clean(self):
        email = self.cleaned_data.get('username')  # This field is renamed as username by Django
        password = self.cleaned_data.get('password')
        if email and password:
            user = authenticate(self.request, username=email, password=password)
            if not user:
                raise forms.ValidationError("Invalid email or password.")
        return self.cleaned_data
