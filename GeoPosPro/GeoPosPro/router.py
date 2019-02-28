from rest_framework import routers
from GeoPosApp.viewsets import ShipViewSet, PosViewSet
from django.urls import path, include
from GeoPosApp import views

router = routers.DefaultRouter()
router.register('ships', ShipViewSet)
router.register('positions', PosViewSet)
#router.register(r'^positions/(?P<id>\d+)', views.Pos1ViewSet.as_view(), base_name = 'blah')
