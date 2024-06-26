from django.shortcuts import render
#from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import region_choices, price_choices, bedroom_choices

# Create your views here.

def index(request):
    listings = Listing.objects.all().order_by('-list_date').filter(is_published=True)[:3]
    context = {'listings' : listings,
               'region_choices': region_choices,
               'price_choices': price_choices,
               'bedroom_choices': bedroom_choices
               }
    return render(request,"pages/index.html", context)

def about(request):
    realtors = Realtor.objects.all().order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = { 
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors}
    return render(request,"pages/about.html", context)
