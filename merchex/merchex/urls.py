from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:band_id>/', views.band_detail, name="band-detail"),
    path('listings/', views.listing_list, name="listing-list"),
    path('listings/<int:list_id>/', views.listing_detail, name="listing-detail"),
    path('about-us/', views.about),
]
