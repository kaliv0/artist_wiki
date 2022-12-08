from artists.api.views import ArtistViewSet, CountryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'countries', CountryViewSet)
urlpatterns = router.urls
