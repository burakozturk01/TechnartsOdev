from rest_framework.routers import DefaultRouter

from .views import AirlineViewSet, AircraftViewSet


router = DefaultRouter()
router.register(r'airline', AirlineViewSet, basename='airline')
router.register(r'aircraft', AircraftViewSet, basename='aircraft')

urlpatterns = router.urls