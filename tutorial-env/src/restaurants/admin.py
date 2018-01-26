from django.contrib import admin

# Register your models here.
from .models import RestaurantLocation,Cuisine

admin.site.register(RestaurantLocation)
admin.site.register(Cuisine)