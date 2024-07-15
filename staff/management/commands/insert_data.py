import json
from datetime import datetime

from django.core.management.base import BaseCommand
from django.db import transaction

from staff.models import Staff


class Command(BaseCommand):
    help = 'Insert data from JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        json_file = options['json_file']

        with open(json_file) as f:
            data = json.load(f)
        with transaction.atomic():
            for item in data:
                start_date = datetime.strptime(item['Start date'], "%Y-%m-%d")
                end_date = datetime.strptime(item['End date'], "%Y-%m-%d")
                data_convert = {
                    'staff_id': item['ID'],
                    'japanese_name': item['Japanese name'],
                    'english_name': item['English name'],
                    'category': item['Category'],
                    'start_date': start_date,
                    'end_date': end_date,
                }
                Staff.objects.create(**data_convert)

        self.stdout.write(self.style.SUCCESS('Data inserted successfully'))
