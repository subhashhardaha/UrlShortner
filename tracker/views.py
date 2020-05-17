from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from analytics.models import ClickEvent
from .models import AffiliateURL
from .utils import ip_address

from .forms import SubmitUrlForm


# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Submit URL",
            "form": the_form
        }
        return render(request, 'tracker/home.html', context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Submit URL",
            "form": form
        }

        template = 'tracker/home.html'

        if form.is_valid():
            #print(form.cleaned_data.get('url'))
            url = form.cleaned_data.get('url')
            obj, created = AffiliateURL.objects.get_or_create(url=url)

            context = {
                "object": obj,
                "created": created
            }

            if created:
                template = 'tracker/success.html'

            else:
                #print(obj.clickevent_set.aggregate(count=Sum('count')))
                context['count']=obj.clickevent_set.aggregate(count=Sum('count'))['count'] or 0
                template = 'tracker/exists.html'

        return render(request, template, context)


class AffiliateCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(AffiliateURL, shortcode=shortcode)
        obj_url = obj.url

        # qs = AffiliateURL.objects.filter(shortcode__iexact=shortcode)
        # if qs.exists() and qs.count() == 1:
        #     obj = qs.first()
        #     obj_url=obj.url
        #print(request.META.get('X_FORWARDED_FOR'))
        #print(request.META.get('REMOTE_ADDR'))
        #print(request.META.get('HTTP_HOST'))
        #print(request.META.get('HTTP_USER_AGENT'))

        request_meta={}
        request_meta['REMOTE_ADDR']=ip_address(request)
        request_meta['HTTP_REFERER']=request.META.get('HTTP_REFERER')
        request_meta['HTTP_USER_AGENT']=request.META.get('HTTP_USER_AGENT')

        #print(request.META)

        # return HttpResponse("hello {sc}".format(sc=obj_url))
        print(ClickEvent.objects.create_event(obj,request_meta))
        return HttpResponseRedirect(obj_url)
