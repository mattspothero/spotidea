from datetime import datetime

from django.test import TestCase
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

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
        json = JSONRenderer().render(resvr_serde.data)
        print(json)
        stream = BytesIO(json)
        data = JSONParser().parse(stream)
        print(data)
        self.assertTrue(False)
