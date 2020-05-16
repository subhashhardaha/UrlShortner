import random
import string

from django.db import models


# Create your models here.

class AffiliateURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=50)
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.url)
