from rest_framework import serializers

from organizer.models import Reservation


class ReservationSerializr(serializers.Serializer):
    start_time = serializers.DateTimeField()
    exit_parking = serializers.DateTimeField()

    class Meta:
        model = Reservation
