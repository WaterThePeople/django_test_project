from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class UserRegisterForm(UserCreationForm):

    error_messages = {
        'password_mismatch': ("Hasła nie są jednakowe!"),
        'min_length': ("Hasło jest za krótkie, musi mieć minimum 8 znaków!"),
    }

    email = forms.EmailField()
    username = forms.CharField(label = 'Nazwa użytkownika',
    required = True,
    error_messages={'invalid': 'Wprowadź prawidłową nazwę użytkownika. Może ona zawierać tylko litery, liczby oraz znaki @/./+/-/_.'},)

    password1 = forms.CharField(label = 'Hasło',
    required = True,
    widget=forms.PasswordInput(),)
    password2 = forms.CharField(label = 'Potwierdź hasło',
    required = True,
    widget=forms.PasswordInput(),)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': ("Nazwa użytkownika lub hasło są nieprawidłowe!"),
    }
    username = forms.CharField(
        label='Nazwa użytkownika',
    )

    password = forms.CharField(
        label='Hasło', 
        widget=forms.PasswordInput(),
    )