from django.db import models
import string
import random

class Url(models.Model):
    short_url = models.CharField(max_length=50)
    long_url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.long_url

    def save(self, *args, **kwargs):
        self.short_url = self.shorten(self.long_url)
        return super(Url, self).save(*args, **kwargs)


# def save(self, *args, **kwargs):
#     super(Profile, self).save(*args, **kwargs)


    @staticmethod
    def shorten(long_url):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
  

