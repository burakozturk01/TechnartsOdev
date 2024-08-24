from rest_framework.routers import DefaultRouter

from .views import AirlineViewSet, AircraftViewSet


router = DefaultRouter()
router.register(r'airline', AirlineViewSet)
router.register(r'aircraft', AircraftViewSet)

urlpatterns = router.urls