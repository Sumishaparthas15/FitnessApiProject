from .models import *
from rest_framework import serializers

class FitnessClassesSerializers(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = '__all__'
