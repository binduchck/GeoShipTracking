from rest_framework import serializers
from GeoPosApp.models import ShipInfo, GeoInfo1


class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipInfo
        fields = '__all__'


class PosSerializer(serializers.ModelSerializer):
    #imo_id = ShipSerializer(source='imo_id')
    #print(imo_id)
    class Meta:
        model = GeoInfo1
        fields = ('imo_id', 'position_timestamp', 'latitude', 'longitude')
