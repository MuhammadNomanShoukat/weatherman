import os
import csv
from weather_app.models import WeatherCharacteristic,Weather,CustomTimeStampModel
from django.core import exceptions


""" reading a files form directory"""
def reading_files(path):
    all_files = []
    """
    loop getting files from path
    sending files to the "all_files" list
    """
    for root, directory, files in os.walk(path):
        """ here finding .txt entention files """
        for file in files:
            if '.txt' in file:
                all_files.append(os.path.join(root, file))
    """ returning the all_files list """
    return all_files

""" sending data to the database fily by bile """
def data_sending_to_database(files):

    for f in list(files):
        with open(f) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_headings = next(csv_reader)

            for row in csv_reader:
                wc = WeatherCharacteristic(max_value=value_validation(row[1]),
                                           min_value=value_validation(row[7]),
                                           avg_value=value_validation(row[3]))
                wc.save()
                w = Weather(weather_date=row[0],
                            temperature=wc,
                            humidity=wc,
                            dew=wc,
                            sea_level_pressure=wc,
                            visibility=wc, wind_velocity=wc,
                            precipitation=value_validation(row[19]),
                            cloud_cover=value_validation(row[20]),
                            events=value_validation(row[21]),
                            wind_dir_degrees=value_validation(row[22]))
                w.save()

""" checking value empty or not here"""
def value_validation(value):

    if value == "":
        value = 0.0
        return value
    else:
        return value







