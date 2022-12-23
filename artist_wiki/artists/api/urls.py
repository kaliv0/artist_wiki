from django.urls import path, include
from rest_framework.routers import DefaultRouter
from artists.api.views import (CountryViewSet, StyleViewSet,
                               FieldViewSet, GenreViewSet,
                               ArtistListCreate, ArtistDetail,
                               ArtworkListCreate, ArtworkDetail)

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'styles', StyleViewSet)
router.register(r'fields', FieldViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('artists/', ArtistListCreate.as_view(), name='artist-list'),
    path('artists/<int:pk>', ArtistDetail.as_view(), name='artist-detail'),
    path('artworks/', ArtworkListCreate.as_view(), name='artwork-list'),
    path('artwork/<int:pk>', ArtworkDetail.as_view(), name='artwork-detail'),
]
