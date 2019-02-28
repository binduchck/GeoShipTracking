from django.db import models

# Create your models here.

class ShipInfo(models.Model):
    imo_id=models.IntegerField(primary_key=True)
    ship_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.ship_name)


class GeoInfo1(models.Model):
    id = models.IntegerField(primary_key=True)
    imo = models.ForeignKey(ShipInfo, on_delete=models.CASCADE)
    position_timestamp = models.DateTimeField()
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

    class Meta:
        ordering = ["-position_timestamp"]

    def __str__(self):
        return str(self.imo)
