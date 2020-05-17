from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from .models import AffiliateURL

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
            print(form.cleaned_data.get('url'))
            url = form.cleaned_data.get('url')
            obj, created = AffiliateURL.objects.get_or_create(url=url)

            context = {
                "object": obj,
                "created": created
            }

            if created:
                template = 'tracker/success.html'

            else:
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
        print(request.META)

        # return HttpResponse("hello {sc}".format(sc=obj_url))
        return HttpResponseRedirect(obj_url)
