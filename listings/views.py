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
        listing = get_object_or_404(Listing,pk=listing_id)
        context = {
            'listing':listing
        }
        return render(request,"listings/listing.html", context)
    except Http404:
        return render(request, '404.html')

def search(request):
    return render(request,"listings/search.html")