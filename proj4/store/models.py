from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class NewNew(models.Model):
    npw = models.CharField(max_length=25)
    def __str__(self):
        return self.site


class Post(models.Model):
    site = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    un = models.CharField(max_length=100)
    pw = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.site

    def get_absoloute_url(self):
        return reverse('post/<int:pk>/', kwargs={'pk' : self.pk})
