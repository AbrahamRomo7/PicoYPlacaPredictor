from django.urls import path
from . import views

urlpatterns =[
    path('index/', views.index),
    path('check-vehicle/', views.check_vehicle, name='check_vehicle')
]