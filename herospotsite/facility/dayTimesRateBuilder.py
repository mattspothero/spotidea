from facility.coroutil import coroutine
from facility.dayTimesRate import DayTimesRate


class DayTimesRateBuilder(object):
    def __init__(self):
        days = 7
        hours = 24
        self._schedule = [[None] * hours for indx in range(days)]

    """python < 3.3 does not allow generator to return"""
    @coroutine
    def populate_schedule(self):
        while True:
            parsed_data = yield
            if parsed_data is None:
                break
            day_indx, start, stop, cost = parsed_data
            start_indx = start.tm_hour
            stop_indx = stop.tm_hour + 1
            day24 = self._schedule[day_indx]
            for hr_indx in range(start_indx, stop_indx):
                day24[hr_indx] = DayTimesRate(day_of_week=day_indx
                                              , start_time=start
                                              , stop_time=stop
                                              , price=cost)

    @property
    def schedule(self):
        return self._schedule
