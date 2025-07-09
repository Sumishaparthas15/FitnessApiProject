# booking/urls.py

from django.urls import path
from . import views

urlpatterns = [
   
    path('classes/', views.FitnessClassListView.as_view(), name='class-list'),
    path('book/', views.BookClass.as_view(), name='book-class'),
    path('bookings/', views.BookingListView.as_view(), name='booking-list'),

]
