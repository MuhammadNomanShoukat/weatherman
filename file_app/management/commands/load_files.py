from django.core.management.base import BaseCommand
from file_app.models import FileData
from django.core import exceptions
import os
import csv


# ========================================== Command Class inheriting BaseCommand ==============================
class Command(BaseCommand):
    help = "Loading files to the database"

    """ this function handling the all operations"""
    def handle(self, *args, **options):

        """ here you have to set you directory(folder) path of you machine """
        path = 'C:\\Users\\Muhammad Noman\\Desktop\\weatherman-master\\weatherfiles'
        files = []

        """ this loop getting all the files from path(directory) and storing into files list """
        for r, d, f in os.walk(path):
            for file in f:
                if '.txt' in file:
                    files.append(os.path.join(r, file))

        count = 0
        """ this loop getting file name from files list and opening it to load data from the file """
        for f in files:
            count = count + 1
            print(count)
            # print(f)
            print("\n=========================== Starting file =====================\n")
            with open(f) as csv_file:
                next(csv_file)
                csv_reader = csv.reader(csv_file, delimiter=',')
                print("MaxT" + "\t" + "MinT" + "\t" + "MaxH" + "\t" + "MeanH" + "\t" + "MinH")
                for row in csv_reader:

                    # """ here we are checking if any field is consist on space(" ") then assign it to 0 """
                    if row[1] == "":
                        row[1] = 0
                    elif row[3] == "":
                        row[3] = 0
                    elif row[7] == "":
                        row[7] = 0
                    elif row[8] == "":
                        row[8] = 0
                    elif row[9] == "":
                        row[9] = 0
                    else:

                    # """ here we are converting fields into integer to store the value into database"""
                        max_t = int(row[1])
                        min_t = int(row[3])
                        max_h = int(row[7])
                        mean_h = int(row[8])
                        min_h = int(row[9])

                    # """ here all data is stroing to the database with integer type """
                        load_data = FileData(file_name=f, max_temp=max_t, min_temp=min_t, max_humd=max_h,
                                             min_humd=min_h, mean_humd=mean_h)
                        load_data.save()
                        self.stdout.write("Data Successfully Save to DataBase")

            print("\n=========================== ending file =====================\n")

