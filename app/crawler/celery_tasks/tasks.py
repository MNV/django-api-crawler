from __future__ import absolute_import, unicode_literals

import logging

from core.celery import app
from crawler.api.api_jael import ApiJael


logger = logging.getLogger(__name__)


@app.task()
def import_hotels():
    """
    Import hotels asynchronously.
    """
    try:
        logger.info('import_hotels')

        api_list = (
            ApiJael(),
        )

        for api_object in api_list:
            import_data.delay(api_object.__class__.__name__)

    except Exception as err:
        logger.error('import_hotels error: {}'.format(err))


@app.task()
def import_data(api_class_name: str):
    """
    Import hotels data.
    :param api_class_name:
    :return:
    """
    class_name = globals()[api_class_name]
    api_object = class_name()
    imported_rows = api_object.process_import()

    logger.info('import_hotels: successfully imported {} rows'.format(imported_rows))
