from app.core.celery import app
from app.crawler.models import Hotel


class ImportService:

    def __init__(self):
        self.hotel_model = Hotel()

    @app.task
    def import_data(self, url):
        pass
