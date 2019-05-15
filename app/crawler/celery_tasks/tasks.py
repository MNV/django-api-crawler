from __future__ import absolute_import, unicode_literals

import logging
from celery.schedules import crontab
from celery.task import periodic_task
from django.core import management

logger = logging.getLogger(__name__)


@periodic_task(run_every=crontab(minute=0, hour=0))
def import_hotels(*args, **kwargs):
    """
    Execute daily at midnight.
    :param args:
    :param kwargs:
    :return:
    """
    try:
        logger.info('import_hotels')
        management.call_command('import_hotels')
    except Exception as err:
        logger.error('import_hotels error: {}'.format(err))
