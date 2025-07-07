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
    

class BookClass(APIView):
    def post(self, request):
        serializer = BookingCreateSerializer(data=request.data)
        if serializer.is_valid():
            class_id = serializer.validated_data['class_id']
            try:
                fitness_class = FitnessClass.objects.get(id=class_id)
                if fitness_class.available_slots <= 0:
                    return Response({'error': 'No available slots'}, status=400)
                
                booking = Booking.objects.create(
                    fitness_class=fitness_class,
                    client_name=serializer.validated_data['client_name'],
                    client_email=serializer.validated_data['client_email']
                )

                fitness_class.available_slots -= 1
                fitness_class.save()

                return Response(BookingSerializer(booking).data, status=201)
            except FitnessClass.DoesNotExist:
                return Response({'error': 'Fitness class not found'}, status=404)
        return Response(serializer.errors, status=400)
    

class BookingListView(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({'error': 'Email is required.'}, status=400)

        bookings = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)    