import maya
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from facility.dayTimesRate import DayTimesRate
from facility.facilityRateParser import FacilityRateParser


class Calculator(APIView):
    _facility_rate = None

    def __init__(self):
        super(Calculator, self).__init__()
        if self._facility_rate is None:
            self._facility_rate = FacilityRateParser().schedule

    def post(self, request):
        start_hour, stop_time, week_day_indx = self.get_data(request)

        rate_found = self._facility_rate[week_day_indx][start_hour]
        assert isinstance(rate_found, DayTimesRate)

        if rate_found is not None and stop_time.hour < rate_found.stop_time.tm_hour:
            return Response(rate_found.price)

        return Response('unavailable')

    def get_data(self, request):
        stream = BytesIO(request.data)
        data = JSONParser().parse(stream)
        start_time = maya.parse(data['start_time'])
        week_day_indx = start_time.weekday - 1  # MayaDT is 1-based for weekday
        start_hour = start_time.hour
        stop_time = maya.parse(data['stop_time'])
        return start_hour, stop_time, week_day_indx
