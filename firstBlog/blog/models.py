from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=60)
    text1 = models.TextField()
    text2 = models.TextField()

