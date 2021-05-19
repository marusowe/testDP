from datetime import datetime
from datetime import timedelta

from celery import shared_task

from config import settings
from urlshort_api.models import UrlShort


@shared_task
def drop_old_rules():
    expired_date = datetime.now().date() - timedelta(days=settings.LINK_EXPIRED_DATE_IN_DAYS)
    return UrlShort.objects.filter(created_at__lte=expired_date).delete()
