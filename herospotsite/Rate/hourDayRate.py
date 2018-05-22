class HourDayRate(object):
    def __init__(self, day_of_week, start_time, end_time, price):
        self._day_of_week = day_of_week
        self._start_time = start_time
        self._end_time = end_time
        self._price = price

    @property
    def day_of_week(self):
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day):
        self.day_of_week = day

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, time):
        self._start_time = time

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        self._end_time = end_time

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price
