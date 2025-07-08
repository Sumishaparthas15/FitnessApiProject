from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.utils.timezone import now
from django.utils.timezone import now, localtime
import logging

logger = logging.getLogger(__name__)

class FitnessClassListView(APIView):
    def get(self, request):
        classes = FitnessClass.objects.filter(datetime__gte=now()).order_by('datetime')
        serializer = FitnessClassesSerializers(classes, many=True)
        for c in serializer.data:
            dt = FitnessClass.objects.get(id=c['id']).datetime
            c['datetime'] = localtime(dt).strftime('%Y-%m-%d %H:%M:%S') 
        return Response(serializer.data)
    

class BookClass(APIView):
    def post(self, request):
        serializer = BookingCreateSerializer(data=request.data)
        if serializer.is_valid():
            class_id = serializer.validated_data['class_id']

            if not isinstance(class_id, int):
                logger.warning("Invalid class_id type received")
                return Response({"error": "class_id must be an integer"}, status=400)

            try:
                fitness_class = FitnessClass.objects.get(id=class_id)
                if fitness_class.available_slots <= 0:
                    logger.error(f"No available slots for class ID: {class_id}")
                    return Response({'error': 'No available slots'}, status=400)

                # Check for duplicate booking
                if Booking.objects.filter(fitness_class=fitness_class, client_email=serializer.validated_data['client_email']).exists():
                    logger.warning(f"Duplicate booking attempt for class ID: {class_id}, email: {serializer.validated_data['client_email']}")
                    return Response({'error': 'You have already booked this class.'}, status=400)

                booking = Booking.objects.create(
                    fitness_class=fitness_class,
                    client_name=serializer.validated_data['client_name'],
                    client_email=serializer.validated_data['client_email']
                )

                fitness_class.available_slots -= 1
                fitness_class.save()

                logger.info(f"Booking created for {serializer.validated_data['client_email']} in class ID: {class_id}")
                return Response(BookingSerializer(booking).data, status=201)

            except FitnessClass.DoesNotExist:
                logger.error(f"Fitness class with ID {class_id} not found")
                return Response({'error': 'Fitness class not found'}, status=404)

        logger.warning(f"Invalid booking request: {serializer.errors}")
        return Response(serializer.errors, status=400)




class BookingListView(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({'error': 'Email is required.'}, status=400)

        bookings = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)    