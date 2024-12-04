import csv
from blog.models import BlogPost
from django.core.management.base import BaseCommand, CommandError
# from ..data import 
class Command(BaseCommand):
    help = 'Import blog posts from a CSV file'

    def add_arguments(self, parser):
        """
            Add logic to add argument for passing the csv file
        """
        parser.add_argument(
            'file_path', 
            type=str, 
            help='The path to the CSV file containing blog posts.'
        )

    def handle(self, *args, **kwargs):
        """
        Populate the database with the data from the CSV file.
        Display errors in red and successful imports in green.
        """
        file_path = kwargs['file_path']

        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        # Validate that required fields are present
                        if 'title' not in row or 'content' not in row:
                            raise ValueError("Missing required fields: 'title' or 'content'.")

                        # Create the blog post
                        BlogPost.objects.create(
                            title=row['title'],
                            content=row['content'],
                            country=row.get('country', None)  # Optional field
                        )
                        self.stdout.write(self.style.SUCCESS(f"Successfully imported: {row['title']}"))

                    except ValueError as ve:
                        self.stderr.write(self.style.ERROR(f"Validation Error: {ve}"))
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f"Error importing row: {e}"))
        
        except FileNotFoundError:
            raise CommandError(f"File not found: {file_path}")
        except Exception as e:
            raise CommandError(f"An error occurred: {e}")

        