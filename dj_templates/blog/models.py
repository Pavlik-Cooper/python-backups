from django.db import models
from django.conf import settings
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=240)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    views = models.IntegerField(default=1)

    def __str__(self):
        return self.title