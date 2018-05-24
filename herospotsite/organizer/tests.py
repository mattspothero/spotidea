import maya
import requests
from django.test import TestCase
from rest_framework.renderers import JSONRenderer

from organizer.models import Reservation
from organizer.serializers import ReservationSerializr

# Create your tests here.


'''Run manage.py test organizer.tests'''


class ReservationTest(TestCase):

    def test_wed_am(self):
        url = 'http://127.0.0.1:8000/find/'
        test_wed_7am = "2015-07-01T07:00:00Z"
        test_wed_12pm = "2015-07-01T12:00:00Z"
        wed_7am = maya.parse(test_wed_7am).datetime()
        wed_12pm = maya.parse(test_wed_12pm).datetime()
        resvr = Reservation(start_time=wed_7am, stop_time=wed_12pm)
        resvr_serde = ReservationSerializr(resvr)
        json = JSONRenderer().render(resvr_serde.data)
        response = requests.post(url=url, json=json)
        self.assertEqual(int(response.text), 1500)

    def test_sat_am(self):
        url = 'http://127.0.0.1:8000/find/'
        test_wed_7am = "2015-07-04T07:00:00Z"
        test_wed_12pm = "2015-07-04T12:00:00Z"
        wed_7am = maya.parse(test_wed_7am).datetime()
        wed_12pm = maya.parse(test_wed_12pm).datetime()
        resvr = Reservation(start_time=wed_7am, stop_time=wed_12pm)
        resvr_serde = ReservationSerializr(resvr)
        json = JSONRenderer().render(resvr_serde.data)
        response = requests.post(url=url, json=json)
        self.assertEqual(int(response.text), 2000)

    def test_sat_pm(self):
        url = 'http://127.0.0.1:8000/find/'
        test_wed_7am = "2015-07-04T07:00:00Z"
        test_wed_12pm = "2015-07-04T20:00:00Z"
        wed_7am = maya.parse(test_wed_7am).datetime()
        wed_12pm = maya.parse(test_wed_12pm).datetime()
        resvr = Reservation(start_time=wed_7am, stop_time=wed_12pm)
        resvr_serde = ReservationSerializr(resvr)
        json = JSONRenderer().render(resvr_serde.data)
        response = requests.post(url=url, json=json)
        self.assertTrue(response.content == '"unavailable"')
