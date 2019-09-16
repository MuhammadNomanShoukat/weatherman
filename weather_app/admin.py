from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from .models import Weather, WeatherCharacteristic


# class SpeciesListFilter(admin.SimpleListFilter):
#     title = 'weather'
#     parameter_name = 'weather'
#
#     default_value = None
#
#     def lookups(self, request, model_admin):
#
#         list_of_species = []
#         queryset = Weather.objects.all()
#         for species in queryset:
#
#             list_of_species.append(
#                 (str(species.id), species.weather_date)
#             )
#         return sorted(list_of_species)
#
#     def queryset(self, request, queryset):
#
#
#         if self.value():
#             return queryset.filter(id=self.value())
#         return queryset
#
#
#
#     def value(self):
#
#         value = super(SpeciesListFilter, self).value()
#         if value is None:
#             if self.default_value is None:
#                 # If there is at least one Species, return the first by name. Otherwise, None.
#                 first_species = Weather.objects.order_by('temperature').first()
#                 value = None if first_species is None else first_species.id
#                 self.default_value = value
#             else:
#                 value = self.default_value
#         return str(value)
#
#
# @admin.register(Weather)
# class BreedAdmin(admin.ModelAdmin):
#     list_display = ('weather_date', 'temperature','humidity','dew','wind_velocity')
#     list_filter = (SpeciesListFilter,)
#

class WeatherCharacteristicAdminClass(admin.ModelAdmin):

    list_display = [
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

    list_filter = [
        'weather_date',
    ]


admin.site.register(WeatherCharacteristic,WeatherCharacteristicAdminClass)
admin.site.register(Weather,WeatherUserAdmin)
