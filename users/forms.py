from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from blog.models import Profile



class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input ', 'placeholder': 'Введите имя пользователя.'}), label='Имя пользователя:')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input ', 'placeholder': 'Введите свой e-mail.'}), label='E-mail пользователя:')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input ', 'placeholder': 'Введите пароль.'}), label='Пароль:')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input ', 'placeholder': 'Повторите пароль.'}), label='Повторить пороль:')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input is-info has-backgound-Light', 'placeholder': 'Введите имя пользователя.'}), label='Имя пользователя:')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-info', 'placeholder': 'Введите пароль.'}), label='Пароль:')

    class Meta:
        model = User
        fields = ['username', 'password']


class EditProfileForm(forms.ModelForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Введите новое имя пользователя.'}), label='Новое  имя пользователя:')
   email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Введите свой новый e-mail.'}), label=' Новый E-mail пользователя:') 
   avatar = forms.ImageField(label='avatar:', required=False)
   password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Введите новый пароль.'}), label=' Новый пароль:')
   password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Повторите новый пароль.'}), label='Повторить новый пороль:')
   
   class Meta:
       model = User
       fields = [ 'username', 'email','avatar', 'password1', 'password2']