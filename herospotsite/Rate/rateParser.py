import json
import os
import time

from Rate.hourDayRate import HourDayRate
from herospotsite import settings

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


class RateParser(object):
    def __init__(self):
        days = 7
        hours = 24
        self._rate_day_hr = [[None] * hours for i in range(days)]

    @property
    def rate_day_hr(self):
        return self._rate_day_hr

    def parse(self):
        rate_dir = os.path.join(settings.BASE_DIR, os.path.dirname(os.path.abspath(__file__)))
        rate_file = os.path.join(rate_dir, 'rate.json')
        assert os.path.exists(rate_file)
        with open(rate_file, 'r') as f:
            rate_data = json.load(f)
            assert isinstance(rate_data, dict)
            rate_list = rate_data.get('rates')
            for r in rate_list:
                assert isinstance(r, dict)
                times = r.get('times').split('-')
                start_time = time.strptime(times[0], '%H%M')
                start_hr = start_time.tm_hour
                end_time = time.strptime(times[1], '%H%M')
                end_hr = end_time.tm_hour + 1
                price = r.get('price')
                days = r.get('days').split(',')
                for d in days:
                    day_indx = DAY_OF_WEEK.get(d.lower())
                    for hr_indx in range(start_hr, end_hr):
                        self._rate_day_hr[day_indx][hr_indx] = HourDayRate(day_indx, start_time, end_time, price)
        return self._rate_day_hr
