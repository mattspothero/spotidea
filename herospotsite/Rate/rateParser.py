import json
import os
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

    def parse(self):
        rate_dir = os.path.join(settings.BASE_DIR, os.path.dirname(os.path.abspath(__file__)))
        rate_file = os.path.join(rate_dir, 'rate.json')
        assert os.path.exists(rate_file)
        with open(rate_file, 'r') as f:
            rate_data = json.load(f)

        return rate_data
