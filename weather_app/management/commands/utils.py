import csv
import logging
import os

from weather_app import models

logger = logging.getLogger(__name__)

def reading_files(path):
    all_files = []
    """
    loop getting files from path
    sending files to the "all_files" list
    """
    for root, directory, weather_files in os.walk(path):
        """ Here finding .txt entention files """
        for input_file in weather_files:
            if '.txt' in input_file:
                all_files.append(os.path.join(root, input_file))

    return all_files


def data_sending_to_database(files):

    for input_file in list(files):
        read_file = csv.DictReader(open(input_file))
        print("Data sending Please wait.")

        for row in read_file:
            """ setting max, min, mean value to the temperature object """
            temperature = models.WeatherCharacteristic(max_value=value_validation(row["Max TemperatureC"]),
                                                       min_value=value_validation(row["Min TemperatureC"]),
                                                       avg_value=value_validation(row["Mean TemperatureC"]))
            temperature.save()
            """ setting max, min, mean value to the dew object """
            dew = models.WeatherCharacteristic(max_value=value_validation(row["Dew PointC"]),
                                               min_value=value_validation(row["Min DewpointC"]),
                                               avg_value=value_validation(row["MeanDew PointC"]))

            dew.save()
            """ setting max, min, mean value to the humidity object """
            humidity = models.WeatherCharacteristic(max_value=value_validation(row["Max Humidity"]),
                                                    min_value=value_validation(row[" Min Humidity"]),
                                                    avg_value=value_validation(row[" Mean Humidity"]))

            humidity.save()
            """ setting max, min, mean value to the sea level pressure object """
            sea_level_pressure = models.WeatherCharacteristic(
                                                        max_value=value_validation(row[" Max Sea Level PressurehPa"]),
                                                        min_value=value_validation(row[" Min Sea Level PressurehPa"]),
                                                        avg_value=value_validation(row[" Mean Sea Level PressurehPa"]))

            sea_level_pressure.save()
            """ setting max, min, mean value to the visibility object """
            visibility = models.WeatherCharacteristic(max_value=value_validation(row[" Max VisibilityKm"]),
                                                      min_value=value_validation(row[" Min VisibilitykM"]),
                                                      avg_value=value_validation(row[" Mean VisibilityKm"]))

            visibility.save()
            """ setting max, min, mean value to the wind velocity object """
            wind_velocity = models.WeatherCharacteristic(max_value=value_validation(row[" Max Wind SpeedKm/h"]),
                                                         min_value=value_validation(0),  # Field not exist in files
                                                         avg_value=value_validation(row[" Mean Wind SpeedKm/h"]))
            wind_velocity.save()
            """ Now sending the object data to the Weather model and other fields """
            weather = models.Weather(weather_date=row["GST"],
                                     temperature=temperature,
                                     humidity=humidity,
                                     dew=dew,
                                     sea_level_pressure=sea_level_pressure,
                                     visibility=visibility,
                                     wind_velocity=wind_velocity,
                                     precipitation=value_validation(row["Precipitationmm"]),
                                     cloud_cover=value_validation(row[" CloudCover"]),
                                     events=value_validation(row[" Events"]),
                                     wind_dir_degrees=value_validation(row["WindDirDegrees"]))
            weather.save()


def value_validation(value):  # This function using for value validation

    if value == "":
        return 0.0
    else:
        return value
