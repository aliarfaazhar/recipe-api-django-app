"""
Waits for db before starting the django app
"""
import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for db...')
        db_ready = False
        while not db_ready:
            try:
                self.check(databases=['default'])
                db_ready = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write(self.style.ERROR('DB not ready'))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('DB ready!'))
