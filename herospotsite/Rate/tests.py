import unittest

# Create your tests here.
from Rate.rateParser import RateParser


class RateTest(unittest.TestCase):

    def test_parse_json(self):
        rp = RateParser()
        result = rp.parse()
        for dayIndx in range(0, 6):
            for hrIndx in range(0, 23):
                hour_day_rate = result[dayIndx][hrIndx]
                if hour_day_rate is not None:
                    print(hour_day_rate)
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
