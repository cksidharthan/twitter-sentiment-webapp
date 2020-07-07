import django
from django.db import models


# Create your models here.
class Search(models.Model):
    search_text = models.CharField(max_length=150, null=False)
    num_tweets = models.IntegerField(default=50)
    from_date = models.CharField(default='2020-05-01', max_length=10)
    language = models.CharField(default='en', max_length=2)
