from django.shortcuts import render
from .models import Band, Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/bands.html',
                  {'bands': bands})
def band_detail(request, band_id):
    # notez le parametre band_id supplementaire permet d'identifier chaque band
    band = Band.objects.get(id=band_id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})
def listing_list(request):
    list = Listing.objects.all()
    return render(request,
                  'listings/listing_list.html',
                  {'items': list})
def listing_detail(request, list_id):
    # notez le parametre band_id supplementaire permet d'identifier chaque band
    list = Listing.objects.get(id=list_id)
    return render(request,
                  'listings/listing_detail.html',
                  {'item': list})
def about(request):
    return HttpResponse("""<h1>hello Django</h1>
<p>je m'appelle Adam chris Kayungura</p>
<p>Mon num +243 994126699 <br> email: adamchrisk@gmail.com</p>
""")
