from rest_framework.test import APITestCase
from django.urls import reverse
from booking.models import FitnessClass, Booking
from django.utils.timezone import make_aware
from datetime import datetime, timedelta

class BookingAPITests(APITestCase):
    def setUp(self):
        self.class1 = FitnessClass.objects.create(
            name='Yoga',
            instructor='Amit',
            datetime=make_aware(datetime.now() + timedelta(days=1)),
            available_slots=10
        )
        self.class2 = FitnessClass.objects.create(
            name='Zumba',
            instructor='Reena',
            datetime=make_aware(datetime.now() + timedelta(days=2)),
            available_slots=0
        )
        
        # ✅ Corrected URLs
        self.booking_url = '/booking/book/'
        self.classes_url = '/booking/classes/'
        self.bookings_url = '/booking/bookings/'


    def test_get_classes(self):
        response = self.client.get(self.classes_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) >= 1)

    def test_successful_booking(self):
        data = {
            "class_id": self.class1.id,
            "client_name": "Sumisha",
            "client_email": "sumisha@example.com"
        }
        response = self.client.post(self.booking_url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 1)

    def test_overbooking(self):
        data = {
            "class_id": self.class2.id,
            "client_name": "Sumisha",
            "client_email": "sumisha@example.com"
        }
        response = self.client.post(self.booking_url, data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('No available slots', str(response.data))
        

    def test_get_bookings_by_email(self):
        Booking.objects.create(
            fitness_class=self.class1,
            client_name="Sumisha",
            client_email="sumisha@example.com"
        )
        response = self.client.get(f'{self.bookings_url}?email=sumisha@example.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
