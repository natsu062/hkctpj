from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Listing 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import region_choices, price_choices, bedroom_choices

# Create your views here.
def index(request):
    listings = Listing.objects.all().order_by('-list_date').filter(is_published=True) 
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {'listings': page_listings}
    return render(request, "listings/listings.html", context)

def listing(request, listing_id):
    try:
        listing = get_object_or_404(Listing, pk=listing_id)
        context = {
            'listing':listing
        }
        return render(request,"listings/listing.html", context)
    except Http404:
        return render(request, '404.html')

def search(request):
    queryset_list = Listing.objects.all().order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    if 'address' in request.GET:
        address = request.GET['address']
        if address:
            queryset_list = queryset_list.filter(address__icontains=address)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    context ={
        'listings' : queryset_list,
        'region_choices' : region_choices, 
        'price_choices' : price_choices,
        'bedroom_choices' : bedroom_choices,
        'values' : request.GET
    }
    return render(request,"listings/search.html", context)