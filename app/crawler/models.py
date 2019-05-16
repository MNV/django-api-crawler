from django.db import models
from django.utils import timezone


class Hotel(models.Model):
    hotel = models.CharField('Hotel', max_length=200)
    country = models.CharField('Country', max_length=20)
    phone = models.CharField('Phone', max_length=20, default=None, blank=True, null=True)
    source = models.CharField('Source', max_length=200)
    raw_data = models.TextField('Data')
    created = models.DateTimeField('Created Date', default=timezone.now)

    def __str__(self):
        return '"{}" in {}'.format(self.hotel, self.country)
