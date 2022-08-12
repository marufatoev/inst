from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}),
                               label='Create any Username')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}),
                             label='Enter your email')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}),
                                label='Enter your password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}),
                                label='Repeat your password')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password1')


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}),
                               label='Enter username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}),
                               label='Enter password')

    class Meta:
        model = User
        fields = ['username', 'password']
