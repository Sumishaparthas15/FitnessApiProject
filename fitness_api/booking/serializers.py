from .models import *
from rest_framework import serializers

class FitnessClassesSerializers(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = '__all__'


class BookingCreateSerializer(serializers.Serializer):
    class_id = serializers.IntegerField()
    client_name = serializers.CharField(max_length=100)
    client_email = serializers.EmailField()


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
