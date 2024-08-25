from rest_framework.response import Response
from rest_framework import viewsets, serializers, status
from rest_framework.decorators import action

from .models import Aircraft, Airline
from .serializers import AircraftListSerializer, AircraftDetailedSerializer, AirlineListSerializer, AirlineDetailedSerializer, CustomTOPSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class BaseViewSet:
    permission_classes = [IsAuthenticated]

class AirlineViewSet(BaseViewSet, viewsets.ModelViewSet):
    queryset = Airline.objects.prefetch_related('aircraft_set').all()
    serializer_class = AirlineDetailedSerializer

    url = serializers.HyperlinkedIdentityField(view_name='airline-detail')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AirlineListSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # If there is a pk (airline_id) in the URL, this code performs the POST deletion operation
        pk = kwargs.get('pk')
        if pk:
            return self.delete_airline(request, pk)
        else:
            # If there is no pk, perform the normal creation operation
            return self.create(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def delete_airline(self, request, pk=None):
        try:
            airline = self.get_object()
            airline.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Airline.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class AircraftViewSet(BaseViewSet, viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftDetailedSerializer

    url = serializers.HyperlinkedIdentityField(view_name='aircraft-detail')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AircraftListSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # If there is a pk (aircraft_id) in the URL, this code performs the POST deletion operation
        pk = kwargs.get('pk')
        if pk:
            return self.delete_aircraft(request, pk)
        else:
            # If there is no pk, perform the normal creation operation
            return self.create(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def delete_aircraft(self, request, pk=None):
        try:
            aircraft = self.get_object()
            aircraft.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Aircraft.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CustomTOPView(TokenObtainPairView):
    serializer_class = CustomTOPSerializer