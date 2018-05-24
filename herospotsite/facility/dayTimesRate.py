import time


class DayTimesRate(object):
    def __init__(self, day_of_week, start_time, stop_time, price):
        self._day_of_week = day_of_week
        self._start_time = start_time
        self._stop_time = stop_time
        self._price = price

    @property
    def day_of_week(self):
        return self._day_of_week

    @property
    def start_time(self):
        return self._start_time

    @property
    def stop_time(self):
        return self._stop_time

    @property
    def price(self):
        return self._price

    def __str__(self):
        return 'Day {} : StartTime {} : EndTime {} : Price {}' \
            .format(self.day_of_week
                    , time.strftime('%H%M', self.start_time)
                    , time.strftime('%H%M', self.stop_time)
                    , self.price)
