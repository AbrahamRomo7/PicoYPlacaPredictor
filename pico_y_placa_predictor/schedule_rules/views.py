from django.shortcuts import render
from datetime import time
from datetime import datetime
#Give us true when the car is allowed to be on road
def liberate_hours(hour):
    morning_start = time(7, 0)  
    morning_end = time(9, 30)    
    evening_start = time(16, 0)   
    evening_end = time(19, 30)    
    if (morning_start <= hour <= morning_end) or (evening_start <= hour <= evening_end):
        return False  
    return True 


#If the day is sturday or sunday the metod give us a False response
def free_days(date):
    if date.weekday() < 5:
        return False
    return True 


def number_of_day(date):
    return date.day
    