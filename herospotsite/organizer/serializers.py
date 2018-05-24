from rest_framework import serializers


class ReservationSerializr(serializers.Serializer):
    start_time = serializers.DateTimeField()
    stop_time = serializers.DateTimeField()
