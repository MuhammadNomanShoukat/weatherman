import os

from django.core.management.base import BaseCommand

from .utils import data_sending_to_database, reading_files


class Command(BaseCommand):
    help = "Loading data from files"

    """ using for weather file argument '"""
    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='Weather file folder name')

    """ command function handling here actions
        1: reading_files()
        2: data_sending_to_database()
        both function are using in it
    """

    def handle(self, *args, **options):
        path_root = os.path.abspath(os.path.dirname(__name__))
        folder_name = options['file_name']

        """ checking here if directory is already exist or not"""
        if not os.path.isdir(folder_name):
            os.mkdir(os.path.join(path_root, folder_name))

        else:
            path = path_root + "\\" + folder_name
            files = reading_files(path)
            data_sending_to_database(files)
