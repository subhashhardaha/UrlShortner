from django.db import models

# Create your models here.

from tracker.models import AffiliateURL


class ClickEventManager(models.Manager):
    def create_event(self, instance,remote_add):
        if isinstance(instance,AffiliateURL):
            obj, created = self.get_or_create(affiliate_url=instance,remote_add=remote_add)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    affiliate_url = models.ForeignKey(AffiliateURL,on_delete=models.CASCADE)
    remote_add = models.GenericIPAddressField(default='127.0.0.1')
    http_referer = models.CharField(null=True,max_length=200)
    http_user_agent = models.CharField(null=True,max_length=200)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{count}".format(count=self.count)
