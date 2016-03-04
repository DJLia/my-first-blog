from django.db import models
from django.utils import timezone

class Post(models.Model):
    owner = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    singer = models.CharField(max_length=200)
    url = models.URLField()
    stars = models.IntegerField()
    registered_date = models.DateTimeField(
                default=timezone.now)

    def publish(self):
        self.registered_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

# Create your models here.
