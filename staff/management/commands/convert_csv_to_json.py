import csv
import json

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    @staticmethod
    def csv_to_json(csv_file_path, json_file_path):
        data = []
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

    def handle(self, *args, **options):
        csv_file_path = "master.csv"
        json_file_path = 'master.json'
        try:
            self.csv_to_json(csv_file_path, json_file_path)
        except Exception as e:
            print(e)
