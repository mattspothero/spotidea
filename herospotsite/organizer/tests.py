from datetime import datetime

from django.test import TestCase
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from organizer.models import Reservation
from organizer.serializers import ReservSerde

import requests

# Create your tests here.


'''Run manage.py test organizer.tests'''


class ReservationTest(TestCase):

    def test_reservation_serializr(self):
        url = 'http://127.0.0.1:8000/find/'
        resvr = Reservation(start_time=datetime.utcnow(), stop_time=datetime.utcnow())
        resvr_serde = ReservSerde(resvr)
        json = JSONRenderer().render(resvr_serde.data)
        response = requests.post(url=url, json=json)
        print(response.text)
        stream = BytesIO(json)
        data = JSONParser().parse(stream)
        print(data)
        self.assertTrue(False)
