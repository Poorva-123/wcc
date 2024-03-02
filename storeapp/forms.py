from django import forms
from .models import TwitterAccount

class TwitterAccountForm(forms.ModelForm):
    class Meta:
        model = TwitterAccount
        fields = ['access_token', 'access_token_secret']

class TweetFilterForm(forms.Form):
    keywords = forms.CharField(label='Keywords', required=False)
