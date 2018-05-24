import os
import time
import unittest

from facility.dayParser import DayParser
from facility.facilityRateParser import FacilityRateParser
from facility.timeParser import TimeParser
from facility.dayTimesRate import DayTimesRate

# Create your tests here.

class DayParserTest(unittest.TestCase):

    def test_parse_day_str(self):
        days = DayParser("mon,tues,wed,thurs,fri")
        self.assertIn(0, days)
        self.assertIn(1, days)
        self.assertIn(2, days)
        self.assertIn(3, days)
        self.assertIn(4, days)
        self.assertNotIn(5, days)
        self.assertNotIn(6, days)

    def test_parse_time_str(self):
        times = TimeParser("0600-1800")
        test_start_time = time.strptime("0600", '%H%M')
        self.assertEqual(test_start_time, times.start_time)
        test_stop_time = time.strptime("1800", '%H%M')
        self.assertEqual(test_stop_time, times.stop_time)

    def test_parse_file_path(self):
        parser = FacilityRateParser()
        rates = parser.rate_list
        self.assertEqual(len(rates), 2)
        parsed_days = DayParser("mon,tues,wed,thurs,fri")
        parsed_times = TimeParser("0600-1800")
        tuple_test = (parsed_days, parsed_times, 1500)
        days_test, times_test, price_test = tuple_test
        self.assertEqual(len(parsed_days.days), 5)
        self.assertEqual(parsed_days, days_test)
        self.assertEqual(parsed_times, times_test)

    def test_sample_facility_rate(self):
        sample_test = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   'sample_facility_rate.json')
        self.assertTrue(os.path.isfile(sample_test))
        rate_parser = FacilityRateParser(sample_test)
        self.assertEqual(len(rate_parser.rate_list), 5)
        self.assertEqual(len(rate_parser.schedule), 7)
        self.assertEqual(len(rate_parser.schedule[0]), 24)
        self.assertEqual(len(rate_parser.schedule[1]), 24)
        self.assertEqual(len(rate_parser.schedule[2]), 24)
        self.assertEqual(len(rate_parser.schedule[3]), 24)
        self.assertEqual(len(rate_parser.schedule[4]), 24)
        self.assertEqual(len(rate_parser.schedule[5]), 24)
        self.assertEqual(len(rate_parser.schedule[6]), 24)

        test_schedule = rate_parser.schedule
        for hr_indx in range(0, 24):
            time_slot = test_schedule[0][hr_indx]
            if hr_indx in [0, 6, 7, 8, 22, 23]:
                self.assertEqual(time_slot, None)
            elif hr_indx in [1, 2, 3, 4, 5]:
                self.assertEqual(time_slot.price, 1000)
            else:
                self.assertEqual(time_slot.price, 1500)
