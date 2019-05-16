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

        if hotels:
            from ..models import Hotel

            for hotel in hotels:
                Hotel.objects.create(
                    hotel=hotel['name'],
                    country=hotel['country'],
                    phone=hotel['phone'],
                    source=self.get_url(),
                    raw_data=hotel,
                )

        return len(hotels)
