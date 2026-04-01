from django.db import models

class Movies(models.Model):
    title = models.CharField(max_lenght=64, unique=True)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True, blank=True)
    director = models.CharField(max_lenght=32)
    producer = models.CharField(max_lenght=128)
    release_date = models.DateField()

    def __str__(self):
        return self.title
