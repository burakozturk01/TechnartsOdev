from rest_framework import viewsets, serializers

from .models import Aircraft, Airline
from .serializers import AircraftSerializer, AirlineSerializer, CustomTOPSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.prefetch_related('aircraft_set').all()
    serializer_class = AirlineSerializer

    permission_classes = [IsAuthenticated]

    url = serializers.HyperlinkedIdentityField(view_name='airline-detail')

class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer

    permission_classes = [IsAuthenticated]

    url = serializers.HyperlinkedIdentityField(view_name='aircraft-detail')

class CustomTOPView(TokenObtainPairView):
    serializer_class = CustomTOPSerializer