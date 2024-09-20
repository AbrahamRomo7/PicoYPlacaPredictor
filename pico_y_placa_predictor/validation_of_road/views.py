from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from sklearn.metrics import auc

from schedule_rules.views import liberate_hours
from license_plate_number.views import validate_plate_and_day
from schedule_rules.views import free_days, liberate_hours

def index(request):
    return render(request,'validation_of_road/index.html')
def be_on_road(plate, date_str, hour_str):
    date = datetime.strptime(date_str, '%Y-%m-%d').date() 
    hour = datetime.strptime(hour_str, '%H:%M').time() 
    if  liberate_hours(hour)==False:
        if free_days(date)==False:
            if validate_plate_and_day(plate, date)==False:
                return False

    return True

def check_vehicle(request):
    if request.method == "POST":
        plate = request.POST.get('plate')
        date = request.POST.get('date')
        hour = request.POST.get('hour')

        can_be_on_road = be_on_road(plate, date, hour)

        return JsonResponse({'can_be_on_road': can_be_on_road})

    return JsonResponse({'error': 'Invalid request'}, status=400)
