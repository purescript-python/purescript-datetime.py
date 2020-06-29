import datetime

createDate = datetime.date


def canonicalDateImpl(ctor, y, m, d):
    date = createDate(y, m, d)
    return ctor(date.year)(date.month)(date.day)


def calcWeekday(y, m, d):
    return createDate(y, m, d).day


def calcDiff(y1, m1, d1, y2, m2, d2):
    dt1 = createDate(y1, m1, d1)
    dt2 = createDate(y2, m2, d2)
    return int((dt1 - dt2).total_seconds() * 1000)
