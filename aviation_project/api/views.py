from rest_framework.response import Response
from rest_framework import viewsets, serializers

from .models import Aircraft, Airline
from .serializers import AircraftListSerializer, AircraftDetailedSerializer, AirlineListSerializer, AirlineDetailedSerializer, CustomTOPSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class BaseViewSet:
    permission_classes = []

class AirlineViewSet(BaseViewSet, viewsets.ModelViewSet):
    queryset = Airline.objects.prefetch_related('aircraft_set').all()
    serializer_class = AirlineDetailedSerializer

    url = serializers.HyperlinkedIdentityField(view_name='airline-detail')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AirlineListSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)

class AircraftViewSet(BaseViewSet, viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftDetailedSerializer

    url = serializers.HyperlinkedIdentityField(view_name='aircraft-detail')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AircraftListSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)

class CustomTOPView(TokenObtainPairView):
    serializer_class = CustomTOPSerializer