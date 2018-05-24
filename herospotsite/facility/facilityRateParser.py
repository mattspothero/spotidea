import json
import os

from facility.dayParser import DayParser
from facility.dayTimesRateBuilder import DayTimesRateBuilder
from facility.timeParser import TimeParser
from herospotsite import settings


class FacilityRateParser(object):
    _rate_list = None
    _schedule = None

    def __init__(self, rate_fp=None):
        if self._rate_list is None:
            self.open_data_file(rate_fp)

        if self._schedule is None:
            self.make_schedule()

    def open_data_file(self, rate_fp):
        if rate_fp is None:
            rate_dir = os.path.join(settings.BASE_DIR,
                                    os.path.dirname(os.path.abspath(__file__)))
            rate_file = os.path.join(rate_dir, 'facility_rate.json')
        else:
            rate_file = rate_fp
        assert os.path.exists(rate_file)

        with open(rate_file, 'r') as f:
            rate_data = json.load(f)
            assert isinstance(rate_data, dict)
            self._rate_list = rate_data.get('rates')
            f.close()

    def make_schedule(self):
        bldr = DayTimesRateBuilder()
        populate_schedule = bldr.populate_schedule()
        for data in self:
            populate_schedule.send(data)
        self._schedule = bldr.schedule

    @property
    def schedule(self):
        return self._schedule

    @property
    def rate_list(self):
        return self._rate_list

    def __iter__(self):
        for r in self._rate_list:
            assert isinstance(r, dict)
            days = DayParser(r.get('days'))
            times = TimeParser(r.get('times'))
            price = int(r.get('price'))
            for indx in days:
                yield indx, times.start_time, times.stop_time, price
