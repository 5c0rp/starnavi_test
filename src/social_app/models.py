from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Model(models.Model):
    class Meta:
        abstract = True

    objects = models.Manager()


class User(AbstractUser):
    last_activity = models.DateTimeField(null=True, blank=True)


class Post(Model):
    class Meta:
        ordering = ['-pub_date']

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=80)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    @property
    def total_likes(self):
        return Like.objects.filter(post=self).count()


class Like(Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    date = models.DateField(auto_now_add=True)
