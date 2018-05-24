import time


class TimeParser(object):
    def __init__(self, timespot):
        self._time_str = timespot.split('-')
        self._start_time = time.strptime(self._time_str[0], '%H%M')
        self._stop_time = time.strptime(self._time_str[1], '%H%M')

    @property
    def start_time(self):
        return self._start_time

    @property
    def stop_time(self):
        return self._stop_time
