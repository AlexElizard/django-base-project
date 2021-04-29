from django.db import models


class Article(models.Model):
    preview_image = models.ImageField("")