from datetime import datetime

from django.test import TestCase

from organizer.models import Reservation
from organizer.serializers import ReservSerde

# Create your tests here.


'''Run manage.py test organizer.tests'''


class ReservationTest(TestCase):

    def test_reservation_serializr(self):
        resvr = Reservation(start_time=datetime.utcnow(), stop_time=datetime.utcnow())
        resvr_serde = ReservSerde(resvr)
        print('start time {}'.format(resvr_serde.data['start_time']))
        print('stop time {}'.format(resvr_serde.data['stop_time']))
        self.assertTrue(False)
