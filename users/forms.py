from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ngettext

class UserRegisterForm(UserCreationForm):

    error_messages = {
       'password_mismatch': ("Hasła nie są jednakowe!"),
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


class CustomPasswordValidator():

    def __init__(self, min_length=5):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "To hasło jest za krótkie, musi posiadać przynajmniej "
                    +str(self.min_length)+" znaków.",
                    "To hasło jest za krótkie, musi posiadać przynajmniej "
                    +str(self.min_length)+" znaków.",
                    self.min_length,
                ),
            )

