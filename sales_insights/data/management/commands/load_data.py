import os
import csv
from django.core.management.base import BaseCommand
from data.models import SalesData

class Command(BaseCommand):
    help = 'Load sales data from a CSV file into the database'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(os.path.dirname(__file__), '../../csv_data/synthetic_sales_data.csv')
        file_path = os.path.abspath(file_path)  # Convert to an absolute path

        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    SalesData.objects.create(
                        date=row['date'],
                        price_per_unit=float(row['price_per_unit']),
                        units_sold=float(row['units_sold'])
                    )
            self.stdout.write(self.style.SUCCESS('Successfully loaded sales data into the database'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {str(e)}"))