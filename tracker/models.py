import random
import string

from django.db import models
from .utils import create_shortcode
from .validators import validate_url

# Create your models here.

class AffiliateURLManager(models.Manager):
    def all(self,*args,**kwarg):
        qs_main=super().all(*args,**kwarg)
        qs=qs_main.filter(active=True)
        return qs

class AffiliateURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url])
    shortcode = models.CharField(max_length=50,unique=True,blank=True)
    sessionid = models.CharField(max_length=50,null=True)
    active=models.BooleanField(default=True)
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    objects=AffiliateURLManager()

    def save(self,*args,**kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode=create_shortcode(self)
        super(AffiliateURL,self).save(*args,**kwargs)

    def get_short_url(self):
        return "http://192.168.0.100/{shortcode}".format(shortcode=self.shortcode)

    def __str__(self):
        return str(self.url)
