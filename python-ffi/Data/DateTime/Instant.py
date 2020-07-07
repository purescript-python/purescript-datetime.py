import datetime
import math


def createUTC(y, mo, d, h, m, s, ms):
    return datetime.datetime(y, mo, d, h, m, s, ms * 1000)


def fromDateTimeImpl(y, mo, d, h, m, s, ms):
    return datetime.datetime(y, mo, d, h, m, s, ms * 1000).timestamp() * 1000


def toDateTimeImpl(ctor):
    def _1(instant):
        date = datetime.datetime.fromtimestamp(instant / 1000)
        return ctor(date.year)(date.month)(date.day)(date.hour)(date.minute)(
            date.second
        )(date.microsecond / 1000)

    return _1
