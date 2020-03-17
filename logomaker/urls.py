from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('listing', views.listing,name='listing'),
    path('listingdetails', views.listingdetails,name='listingdetails'),
   
    
    
 ]