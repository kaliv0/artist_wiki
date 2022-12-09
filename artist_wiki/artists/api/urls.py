from rest_framework.routers import DefaultRouter
from artists.api.views import (ArtistViewSet, CountryViewSet,
                               StyleViewSet, FieldViewSet,
                               GenreViewSet, ArtworkViewSet)

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'styles', StyleViewSet)
router.register(r'fields', FieldViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'artworks', ArtworkViewSet)
router.register(r'artists', ArtistViewSet)
urlpatterns = router.urls
