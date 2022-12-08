from django.contrib import admin

from artists.models import Artist, Country, Style

admin.site.register(Country)
admin.site.register(Style)
admin.site.register(Artist)
