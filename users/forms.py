from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from blog.models import Profile



class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-rounded is-info', 'placeholder': 'Введите имя пользователя.'}), label='Имя пользователя:')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input is-rounded is-info', 'placeholder': 'Введите свой e-mail.'}), label='E-mail пользователя:')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-rounded is-info', 'placeholder': 'Введите пороль.'}), label='Пароль:')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-rounded is-info', 'placeholder': 'Повторите пороль.'}), label='Повторить пороль:')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-rounded is-info', 'placeholder': 'Введите имя пользователя.'}), label='Имя пользователя:')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-rounded is-info', 'placeholder': 'Введите пороль.'}), label='Пароль:')

    class Meta:
        model = User
        fields = ['username', 'password']


class EditProfileForm(forms.ModelForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-rounded is-info', 'placeholder': 'Введите новое имя пользователя.'}), label='Новое  имя пользователя:')
   email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input is-rounded is-info', 'placeholder': 'Введите свой новый e-mail.'}), label=' Новый E-mail пользователя:')
   password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-rounded is-info', 'placeholder': 'Введите новый пороль.'}), label=' Новый пароль:')
   password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-rounded is-info', 'placeholder': 'Повторите новый пороль.'}), label='Повторить новый пороль:')

   class Meta:
       model = User
       fields = [ 'username', 'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'input is-rounded is-info mb-5', 'placeholder': 'Введите новое имя пользователя.'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class': 'input is-rounded is-info ', 'placeholder': 'Введите новую почту пользователя.'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(label='Картинка:', required=False)
    bio = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'input  is-info', 'placeholder': 'Введите немного о себе.'}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
