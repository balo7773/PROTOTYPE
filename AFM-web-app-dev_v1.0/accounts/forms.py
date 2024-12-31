# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
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
