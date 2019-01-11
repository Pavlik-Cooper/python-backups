import pytz
import datetime

from django.utils import timezone
from django.conf import settings
from django.utils.timezone import make_aware

naive_datetime = datetime.datetime.now()
naive_datetime.tzinfo  # None

settings.TIME_ZONE  # 'UTC'

# convert to aware
aware_datetime = make_aware(naive_datetime)
aware_datetime.tzinfo

# or
aware_datetime = datetime.datetime(2015, 1, 1, tzinfo=timezone.utc)

# or
aware_datetime = datetime.datetime(2015, 1, 1, tzinfo=pytz.UTC)
