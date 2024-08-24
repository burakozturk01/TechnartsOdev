from rest_framework import viewsets

from .models import Aircraft, Airline
from .serializers import AircraftSerializer, AirlineSerializer

# Create your views here.
class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer