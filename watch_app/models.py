from django.db import models

class StreamPlatform(models.Model):
    platform_name = models.CharField(max_length=50)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.platform_name

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

