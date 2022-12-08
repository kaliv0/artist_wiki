from artists.api.views import ArtistViewSet, CountryViewSet, StyleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'styles', StyleViewSet)
urlpatterns = router.urls
