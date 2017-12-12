from datetime import datetime
import dateutil.parser
import time
import logging
from tzlocal import get_localzone
import pytz

logger = logging.getLogger(__name__)


def normalize_timestamp(date_time):
    """
    Attempt to convert a string timestamp in to a TruSTAR compatible format for submission.
    Will return current time with UTC time zone if None
    :param date_time: int that is epoch time, or string/datetime object containing date, time, and ideally timezone
    examples of supported timestamp formats: 1487890914, 1487890914000, "2017-02-23T23:01:54",
    "2017-02-23T23:01:54+0000"
    """
    datetime_dt = datetime.now()

    # get current time in seconds-since-epoch
    current_time = int(time.time())

    try:
        # identify type of timestamp and convert to datetime object
        if isinstance(date_time, int):

            # if timestamp has less than 10 digits, it is in seconds
            if date_time < 10000000000:
                date_time *= 1000

            # if timestamp is incorrectly forward dated, set to current time
            if date_time > current_time:
                raise ValueError("The given time %s is in the future." % date_time)

            datetime_dt = datetime.fromtimestamp(date_time)
        elif isinstance(date_time, str):
            datetime_dt = dateutil.parser.parse(date_time)
        elif isinstance(date_time, datetime):
            datetime_dt = date_time

    # if timestamp is none of the formats above, error message is printed and timestamp is set to current time by
    # default
    except Exception as e:
        logger.warn(e)
        logger.warn("Using current time as replacement.")
        datetime_dt = datetime.now()

    # if timestamp is timezone naive, add timezone
    if not datetime_dt.tzinfo:
        # add system timezone and convert to UTC
        datetime_dt = get_localzone().localize(datetime_dt).astimezone(pytz.utc)

    # converts datetime to iso8601
    return datetime_dt.isoformat()