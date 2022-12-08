from django.contrib import admin

from artists.models import Artist, Country

admin.site.register(Country)
admin.site.register(Artist)
