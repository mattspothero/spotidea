from __future__ import unicode_literals


# Create your models here.
class Reservation(object):
    def __init__(self, start_time, stop_time):
        self.start_parking = start_time
        self.stop_parking = stop_time

    @property
    def start_time(self):
        return self.start_parking

    @start_time.setter
    def start_time(self, enter_time):
        self.start_parking = enter_time

    @property
    def stop_time(self):
        return self.stop_parking

    @stop_time.setter
    def stop_time(self, stop_time):
        self.stop_parking = stop_time

    def __repr__(self):
        day_of_week = self.start_time.weekday()
        hour_start = self.start_time.hour
        min_start = self.start_time.minute
        iso_start = self.start_time.isoformat()
        return 'start parking at {} \n day_of_week: {} \n hh: {} \n mm: {}'.format(iso_start, day_of_week, hour_start,
                                                                                   min_start)
