from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter Username"}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter Email"}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Password"}
        )
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ]


class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter Username"}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Password"}
        )
    )