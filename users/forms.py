from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Создайте любое имя пользователя')
   password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label='Введите пароль')
   password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label='Подтвердите пароль')

   class Meta:
       model = User
       fields = ['username', 'password1', 'password2']

class SignInForm(AuthenticationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Логин')
   password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label='Пароль')

   class Meta:
       model = User
       fields = ['username', 'password']