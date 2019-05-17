import requests

from .api_base import ApiBase


class ApiJael(ApiBase):
    """
    Hotels API integration.
    https://github.com/leejaew/api.jael.ee/blob/master/hotels.md
    """

    def get_url(self) -> str:
        return 'https://api.jael.ee/datasets/hotels'

    def process_import(self) -> int:
        params = {'country': 'singapore'}
        r = requests.get(self.get_url(), params=params)
        hotels = r.json()

        imported_rows = 0
        if hotels:
            from ..models import Hotel

            for hotel in hotels:
                if not Hotel.objects.filter(hotel=hotel['name'], country=hotel['country']).exists():
                    Hotel.objects.create(
                        hotel=hotel['name'],
                        country=hotel['country'],
                        phone=hotel['phone'],
                        source=self.get_url(),
                        raw_data=hotel,
                    )
                    imported_rows += 1

        return imported_rows
