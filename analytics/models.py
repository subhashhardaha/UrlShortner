from django.db import models

# Create your models here.

from tracker.models import AffiliateURL


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(AffiliateURL, instance):
            obj, created = self.objects.get_or_create(affiliate_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    affiliate_url = models.ForeignKey(AffiliateURL,on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return self.count
