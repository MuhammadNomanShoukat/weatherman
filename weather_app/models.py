# This file will contain user models
from django.db import models


# Create your models here.


class CustomTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class WeatherCharacteristic(CustomTimeStampModel):
    min_value = models.DecimalField(max_digits=5, decimal_places=1)
    max_value = models.DecimalField(max_digits=5, decimal_places=1)
    avg_value = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return f"max={self.max_value},  mean={self.avg_value},  min={self.min_value}"


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

    def __str__(self):
        return f"{self.weather_date}"
