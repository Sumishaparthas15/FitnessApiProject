# booking/urls.py

from django.urls import path
from . import views

urlpatterns = [
   
    path('classes/', views.FitnessClassListView.as_view(), name='class-list'),
]
