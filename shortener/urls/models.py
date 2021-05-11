from django.db import models
import random

class Url(models.Model):
    short_url = models.CharField(max_length=50, unique=True)
    long_url = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.short_url

    # def save(self):
    #     return super().save()

    # @classmethod
    # def shorten(long_url):
    #     ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    #     return 

