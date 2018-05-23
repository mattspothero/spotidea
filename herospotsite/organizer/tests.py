import unittest
from datetime import date
from datetime import datetime

from organizer.models import Reservation


# Create your tests here.


class ReservationTest(unittest.TestCase):

    def test_reservation_serializr(self):
        resvr = Reservation(start_time=datetime.utcnow(), stop_time=date.today().isoformat())
        print(resvr)
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
