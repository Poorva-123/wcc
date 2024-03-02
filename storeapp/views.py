from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ChildTwitterAccount, TwitterAccount
from .forms import TwitterAccountForm,TweetFilterForm
from .twitter_utils import get_tweets, filter_tweets, get_twitter_auth, get_access_tokens

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    form = TweetFilterForm(request.POST or None)
    tweets = []
    filtered_tweets = []
    twitter_linked = False

    try:
        # Get the child's Twitter account associated with the current user
        child_twitter_account = ChildTwitterAccount.objects.get(user=request.user)
        twitter_linked = True

        if request.method == 'POST' and form.is_valid():
            keywords = form.cleaned_data.get('keywords')
            # Fetch tweets from the child's Twitter account based on the filtering criteria
            tweets = get_tweets(child_twitter_account.twitter_username)
            # Filter tweets based on the provided keywords
            filtered_tweets = filter_tweets(tweets, keywords)

        else:
            # Fetch tweets from the child's Twitter account
            tweets = get_tweets(child_twitter_account.twitter_username)
            # No filtering applied by default
            filtered_tweets = tweets

    except ChildTwitterAccount.DoesNotExist:
        pass  # Handle the case where the child's Twitter account is not found

    return render(request, 'dashboard.html', {'form': form, 'tweets': tweets, 'filtered_tweets': filtered_tweets, 'twitter_linked': twitter_linked})

def link_twitter_account(request):
    if request.method == 'POST':
        form = TwitterAccountForm(request.POST)
        if form.is_valid():
            twitter_account = form.save(commit=False)
            twitter_account.user = request.user
            twitter_account.save()
            return redirect('dashboard')
    else:
        form = TwitterAccountForm()
    return render(request, 'link_twitter_account.html', {'form': form})

def twitter_callback(request):
    # Your view logic here
    return render(request, 'twitter_callback.html')

def terms_of_service(request):
    # Render the terms of service template
    return render(request, 'terms_of_service.html')
