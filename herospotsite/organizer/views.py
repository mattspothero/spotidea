from django.utils.six import BytesIO
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def findspot(request):
    stream = BytesIO(request.data)
    data = JSONParser().parse(stream)
    print('Stop time : {}'.format(data['start_time']))
    print('Stop time : {}'.format(data['stop_time']))
    return Response('Found spot')
