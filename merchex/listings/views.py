from django.shortcuts import render, redirect, HttpResponse
from .models import Band, Listing
from .forms import ContactUsForm
from django.core.mail import send_mail
from listings.forms import BandForm, ListingForm

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
def band_create(request):
    choice = 'band'
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request,
                  'listings/create.html',
                  {'form': form,
                   'choice':choice})
def listing_create(request):
    choice='listing'
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    return render(request,
                  'listings/create.html',
                  {'form': form,
                   'choice':choice})
def band_update(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        form = BandForm(request.POST,
                        instance=band)
        if form.is_valid():
            form.save()
            return  redirect('band-detail', band.id)
    form = BandForm(instance=band)
    return  render(request,
                   'listings/band_update.html',
                   {'form': form,
                    'band': band})
def listing_update(request, list_id):
    listing = Listing.objects.get(id=list_id)
    if request.method == 'POST':
        form = ListingForm(request.POST,
                        instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing-detail', listing.id)
    form = ListingForm(instance=listing)
    return render(request,
                   'listings/listing_update.html',
                   {'form': form})
def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
    return render(request,
                   'listings/delete.html',
                   {'item': band})

def listing_delete(request, list_id):
    list = Listing.objects.get(id=list_id)
    if request.method == 'POST':
        list.delete()
        return redirect('listing-list')
    return render(request,
                   'listings/delete.html',
                   {'item': list})


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message de {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact-us Form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'])
            return redirect('band-list')
    else:
        form = ContactUsForm()
    return render(request,
                  'listings/contact.html',
                  {'form': form})
def about(request):
    return render(request,
                  'listings/about.html')
