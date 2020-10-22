from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=100, default=None)
    image = models.ImageField(default='default.png', blank=True)
    text = models.TextField(blank=True)
    source_code = models.CharField(max_length=100, default=None, blank=True)
    live_view = models.CharField(max_length=100, default=None, blank=True)

    def __str__(self):
        return self.title
