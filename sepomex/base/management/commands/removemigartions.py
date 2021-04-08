import os

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'Remove migrations'

    def __validate_file(
            self,
            file_name: str,
    ) -> bool:
        if file_name.startswith('__'):
            return False
        return True

    def handle(self, *args, **options):
        for app_directory in settings.INSTALLED_APPS:
            if not os.path.isdir(app_directory):
                continue
            directory = app_directory + '/migrations/'
            if not os.path.isdir(directory):
                continue
            files = os.listdir(directory)
            files_to_remove = [
                x
                for x in files
                if self.__validate_file(x)
            ]
            removed_migrations = len(files_to_remove)
            [
                os.remove(directory + x)
                for x in files_to_remove
            ]
            self.stdout.write(
                self.style.SUCCESS(
                    'Successfully removed %d migrations of the app "%s"' % (removed_migrations,  app_directory)
                )
            )
