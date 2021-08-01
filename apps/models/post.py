from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), blank=True)

    def __str__(self):
        return self.title
