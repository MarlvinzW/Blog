from django import forms
from .models import Articles


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'body']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=255, help_text='Search for an article')

