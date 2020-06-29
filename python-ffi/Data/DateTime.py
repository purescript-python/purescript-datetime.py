import datetime
import math


def createUTC(y, mo, d, h, m, s, ms):
    return datetime.datetime(y, mo, d, h, m, s, ms * 1000)


def calcDiff(rec1, rec2):
    msUTC1 = createUTC(
        rec1["year"],
        rec1["month"],
        rec1["day"],
        rec1["hour"],
        rec1["minute"],
        rec1["second"],
        rec1["millisecond"],
    )
    msUTC2 = createUTC(
        rec2["year"],
        rec2["month"],
        rec2["day"],
        rec2["hour"],
        rec2["minute"],
        rec2["second"],
        rec2["millisecond"],
    )
    return msUTC1 - msUTC2


def adjustImpl(just):
    def _1(nothing):
        def _2(offset):
            def _3(rec):
                msUTC = createUTC(
                    rec["year"],
                    rec["month"],
                    rec["day"],
                    rec["hour"],
                    rec["minute"],
                    rec["second"],
                    rec["millisecond"],
                )
                dt = msUTC + offset
                return (
                    nothing
                    if math.isnan(dt.timestamp() * 1000)
                    else just(
                        {
                            "year": dt.year,
                            "month": dt.month,
                            "day": dt.day,
                            "hour": dt.hour,
                            "minute": dt.minute,
                            "second": dt.second,
                            "millisecond": dt.microsecond / 1000,
                        }
                    )
                )

            return _3

        return _2

    return _1

