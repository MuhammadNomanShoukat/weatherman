from django.core.management.base import BaseCommand
import os
import csv
from .utils import reading_files,data_sending_to_database

""" Base Command class  """
class Command(BaseCommand):
    help = "Loading data from files"
    """ 
    command function handling here actions
    1: reading_files()
    2: data_sending_to_database()
    both function are using in it
    """
    def handle(self, *args, **options):
        path_root = os.path.abspath(os.path.dirname(__name__))
        folder_name = "weatherfiles"
        path = path_root + "\\" + folder_name
        """ using for reading files form directory and returning back to files """
        files = reading_files(path)
        """ using for sending data to the database """
        data_sending_to_database(files)

