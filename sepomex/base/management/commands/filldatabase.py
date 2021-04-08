from typing import Type, Tuple

from django.core.management import BaseCommand

from base.entities.db_filler_interface import DBFillerInterface
from codigos_postales.entities.codigos_postales_db_filler import CodigosPostalesDBFiller
# from users.entities.users_db_filler import UsersDBFiller


class Command(BaseCommand):

    FILLERS: Tuple[Type[DBFillerInterface]] = (
        CodigosPostalesDBFiller,
        # UsersDBFiller,
    )

    help = 'Fills database'

    def handle(self, *args, **options):
        for filler_class in self.FILLERS:
            filler: DBFillerInterface = filler_class()
            filler.fill_database()
        self.stdout.write(self.style.SUCCESS('Se populó la base de datos exitosamente'))
