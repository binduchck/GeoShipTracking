from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from GeoPosApp.models import GeoInfo1, ShipInfo
from GeoPosApp.serializer import ShipSerializer, PosSerializer


class ShipViewSet(viewsets.ModelViewSet):
    queryset = ShipInfo.objects.all()
    serializer_class = ShipSerializer


class PosViewSet(viewsets.ModelViewSet):
    queryset = GeoInfo1.objects.all()
    serializer_class = PosSerializer
    #lookup_field = 'imo_id'
