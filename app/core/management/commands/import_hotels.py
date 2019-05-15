from django.core.management.base import BaseCommand

from app.crawler.services.import_service import ImportService


class Command(BaseCommand):
    """Import hotels data via APIs"""

    help = 'Set period for updated textbook\'s files.'

    API_URLS = (
        'https://api.jael.ee/datasets/hotels',
    )

    def __init__(self):
        super().__init__()
        self.import_service = ImportService()

    def handle(self, *args, **options):

        self.stdout.write('Hotels data updating...')

        for url in self.API_URLS:
            self.import_service.import_data.delay(url)
