import argparse
from django.core.management.base import BaseCommand, CommandError
from user.models import Member, ActivityPeriod

import factory

from ...factory import ActivityPeriodFactory

class Command(BaseCommand):
    '''
    Custom management Command to populate data
    to run : python manage.py populate [num]
    [num] = number of data to be made at a time

    '''
    help = 'Populate the database'

    def add_arguments(self, parser):
        parser.add_argument('num', nargs = "?",default= 10, type=int) # num is the number of data to be made at a time

    def handle(self, *args, **options):
        factory.build_batch(ActivityPeriodFactory, size = options['num'])
        self.stdout.write(self.style.SUCCESS('Successfully generated fields'))
