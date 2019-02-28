from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from GeoPosApp.models import GeoInfo1, ShipInfo
from GeoPosApp.serializer import ShipSerializer, PosSerializer

# Create your views here.
class Pos1View(generics.ListAPIView):
    serializer_class = PosSerializer

    def get_queryset(self):
        return GeoInfo1.objects.filter(imo_id=self.kwargs['imo'])
