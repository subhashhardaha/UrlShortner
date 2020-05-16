from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import AffiliateURL


# Create your views here.

def affiliate_redirect_views(request, shortcode=None, *args, **kwargs):

    obj=get_object_or_404(AffiliateURL,shortcode=shortcode)
    obj_url=obj.url

    # qs = AffiliateURL.objects.filter(shortcode__iexact=shortcode)
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url=obj.url

    return HttpResponse("hello {sc}".format(sc=obj_url))
