from django.contrib import admin

from .models import Aircraft, Airline

# Register your models here.
admin.site.register(Aircraft)
admin.site.register(Airline)
