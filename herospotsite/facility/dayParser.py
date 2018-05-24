#      "days": "mon,tues,wed,thurs,fri,sat,sun"
DAY_OF_WEEK = {
    'mon': 0,
    'tues': 1,
    'wed': 2,
    'thurs': 3,
    'fri': 4,
    'sat': 5,
    'sun': 6
}


class DayParser(object):
    def __init__(self, dayStr):
        self._daystr = dayStr
        self._days = dayStr.split(',')

    def __repr__(self):
        return 'Days {}'.format(self.days)

    def __iter__(self):
        for day in self._days:
            yield DAY_OF_WEEK.get(day.lower())

    @property
    def days(self):
        return self._days
