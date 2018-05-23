from rest_framework import serializers


class ReservSerde(serializers.Serializer):
    start_time = serializers.DateTimeField()
    stop_time = serializers.DateTimeField()
