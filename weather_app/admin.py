from django.contrib import admin
from .models import WeatherCharacteristic,Weather


class WeatherCharacteristicAdminClass(admin.ModelAdmin):

    list_display = [
        'max_value',
        'min_value',
        'avg_value',
    ]

    list_filter = [
        'max_value',
        'min_value',
        'avg_value',
    ]

class WeatherUserAdmin(admin.ModelAdmin):
    list_display = [
        'weather_date',
        'temperature',
        'humidity',
    ]

admin.site.register(WeatherCharacteristic,WeatherCharacteristicAdminClass)
admin.site.register(Weather,WeatherUserAdmin)