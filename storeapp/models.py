from django.db import models
from django.contrib.auth.models import User

class ChildTwitterAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    twitter_username = models.CharField(max_length=100, blank=True, null=True)

class FlaggedTweet(models.Model):
    tweet_id = models.CharField(max_length=100)
    content = models.TextField()
    flagged_at = models.DateTimeField(auto_now_add=True)

class TwitterAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    access_token_secret = models.CharField(max_length=255)

    def __str__(self):
        return f"Twitter Account for {self.user.username}"
