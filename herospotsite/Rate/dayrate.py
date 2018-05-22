class Dayrate(object):
    def __init__(self, day_of_week, start_time):
        self._day_of_week = day_of_week
        self._start_time = start_time

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
