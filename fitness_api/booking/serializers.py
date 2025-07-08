from .models import *
from rest_framework import serializers
from django.utils.timezone import localtime


class FitnessClassesSerializers(serializers.ModelSerializer):
    datetime = serializers.SerializerMethodField()

    class Meta:
        model = FitnessClass
        fields = '__all__'

    def get_datetime(self, obj):
        return localtime(obj.datetime).strftime('%Y-%m-%d %H:%M:%S')

class BookingCreateSerializer(serializers.Serializer):
    class_id = serializers.IntegerField()
    client_name = serializers.CharField(max_length=100)
    client_email = serializers.EmailField()


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
