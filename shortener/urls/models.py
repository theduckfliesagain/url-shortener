from django.db import models


class Url(models.Model):
    short_url = models.CharField(max_length=50)
    long_url = models.CharField(max_length=200)
    
    def __str__(self):
        return self.short_url
