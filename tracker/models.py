import random
import string

from django.db import models

def code_generator(size=6,char=string.ascii_letters+string.digits):
    return ''.join(random.choice(char) for _ in range(size))

# Create your models here.

class AffiliateURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=50)
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)


    def save(self,*args,**kwargs):
        self.shortcode=code_generator()
        super(AffiliateURL,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.url)
