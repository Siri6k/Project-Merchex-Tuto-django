from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # afficahage en liste et en detail des groupes et des annonces
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:band_id>/', views.band_detail, name="band-detail"),
    path('listings/', views.listing_list, name="listing-list"),
    path('listings/<int:list_id>/', views.listing_detail, name="listing-detail"),
    # creation d'une bande et des annonces
    path('bands/add/', views.band_create, name="band-create"),
    path('listings/add/', views.listing_create, name="listing-create"),
    #Modiffiez un groupe et une annonce sur le site
    path('bands/<int:band_id>/change/', views.band_update, name="band-update"),
    path('listings/<int:list_id>/change/', views.listing_update, name="listing-update"),
    # effacer un objet de la base des données
    path('bands/<int:band_id>/delete/', views.band_delete, name="band-delete"),
    path('listings/<int:list_id>/delete/', views.listing_delete, name="listing-delete"),

    # contactez nous
    path('contact/', views.contact, name="contact-us"),
    path('about/', views.about, name="about-us"),
]
