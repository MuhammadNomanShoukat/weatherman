from __future__ import unicode_literals
from django.db import models
import uuid

""" Custiom time stamp model """
class CustomTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    """ using to set class abstract for to create a model """
    class Meta:
        abstract = True

""" Weather Characteristics model """
class WeatherCharacteristic(CustomTimeStampModel):
    min_value = models.DecimalField(max_digits=5, decimal_places=1)
    max_value = models.DecimalField(max_digits=5, decimal_places=1)
    avg_value = models.DecimalField(max_digits=5, decimal_places=1)

    """ return back fields to the admin panel """
    def __str__(self):
        return r"{0} - {1} - {2}".format(self.min_value,self.max_value,self.avg_value)

""" Weather model """
class Weather(CustomTimeStampModel):
    weather_date = models.DateField(unique=True)
    temperature = models.OneToOneField(WeatherCharacteristic, on_delete=models.CASCADE, related_name='+')
    humidity = models.OneToOneField(WeatherCharacteristic, on_delete=models.CASCADE, related_name='+')
    dew = models.OneToOneField(WeatherCharacteristic, on_delete=models.CASCADE, related_name='+')
    sea_level_pressure = models.OneToOneField(WeatherCharacteristic, on_delete=models.CASCADE, related_name='+')
    visibility = models.OneToOneField(WeatherCharacteristic, on_delete=models.CASCADE, related_name='+')
    wind_velocity = models.OneToOneField(WeatherCharacteristic, on_delete=models.CASCADE, related_name='+')
    precipitation = models.CharField(max_length=5,default="")
    cloud_cover = models.CharField(max_length=5, default="")
    events = models.CharField(max_length=5, default="")
    wind_dir_degrees = models.CharField(max_length=5, default="")

    """ return back weather date to admin panel """
    def __str__(self):
        return r"{0}".format(self.weather_date)
