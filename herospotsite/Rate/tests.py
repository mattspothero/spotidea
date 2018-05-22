import unittest
# Create your tests here.
from Rate.rateParser import RateParser


class RateTest(unittest.TestCase):

    def test_parse_json(self):
        rp = RateParser()
        result = rp.parse()
        self.assertTrue(isinstance(result, dict))


if __name__ == '__main__':
    unittest.main()
