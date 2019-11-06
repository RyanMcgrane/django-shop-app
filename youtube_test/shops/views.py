from django.core import serializers
from django.http import HttpResponse
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View

from .models import Shop
import json

# Create your views here.

longitude = -6.2603
latitude = 53.3498

user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(
    distance=Distance('location', user_location)
    ).order_by('distance')[0:6]
    template_name = 'shops/'


def index(request):
    template = 'shops/index1.html'
    results = Shop.objects.all()
    jsondata = serializers.serialize('json', results)
    context = {
        'results': results,
        'jsondata': jsondata,
    }
    return render(request, template, context)


def getdata(request):
    results = Shop.objects.all()
    jsondata = serializers.serialize('json', results)
    return HttpResponse(jsondata)


def base_layout(request):
    template = 'shops/base.html'
    return render(request, template)


def shop_map(request):
    template = 'shops/shopMap.html'
    return render(request, template)


home = Home.as_view()
