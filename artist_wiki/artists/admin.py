from django.contrib import admin

from artists.models import (Artist, Country,
                            Style, Field,
                            Genre, Artwork)

admin.site.register(Country)
admin.site.register(Style)
admin.site.register(Field)
admin.site.register(Genre)
admin.site.register(Artwork)
admin.site.register(Artist)
