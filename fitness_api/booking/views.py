from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.utils.timezone import now

class FitnessClassListView(APIView):
    def get(self, request):
        classes =  FitnessClass.objects.filter(datetime__gte =now()).order_by('datetime')
        serializer = FitnessClassesSerializers(classes,many = True)
        return Response(serializer.data)
    

    
