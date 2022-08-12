from django import forms
from . import models


class ArticleFrom(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'class':'textarea', 'size': '40'}))

    class Meta:
        model= models.Article
        fields = ['title', 'text', 'thumb']


class Create(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'class':'textarea', 'size': '10' }))
    
    class Meta:
        model= models.Article
        fields = ['title', 'text', 'thumb']


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'textarea',
        'size':'40',
        'placeholder': 'Напишите свой комментарий здесь...'
    }))


    class Meta:
        model = models.Comment
        fields = ['body',]