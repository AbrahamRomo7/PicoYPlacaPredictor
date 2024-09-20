from django.shortcuts import render
from schedule_rules.views import number_of_day

def get_last_digit(plate):
    return plate[-1]

#If the license plate number is on the day of restriction return false
def validate_plate_and_day(plate, date):
    last_digit = get_last_digit(plate)
    day_number = number_of_day(date)

    # Determinar si el vehículo no puede circular
    if last_digit in ['1', '2']:
        return day_number != 0  # Lunes
    elif last_digit in ['3', '4']:
        return day_number != 1  # Martes
    elif last_digit in ['5', '6']:
        return day_number != 2  # Miércoles
    elif last_digit in ['7', '8']:
        return day_number != 3  # Jueves
    elif last_digit in ['9', '0']:
        return day_number != 4  # Viernes

    # Si no coincide con ninguna restricción
    return True
"""def validate_plate_and_day(plate, date):
    last_digit = get_last_digit(plate)
    day_number = number_of_day(date)

    restriction_map = {
        '1': 0,
        '2': 0,
        '3': 1,
        '4': 1,
        '5': 2,
        '6': 2,
        '7': 3,
        '8': 3,
        '9': 4,
        '0': 4
    }

    return  day_number != restriction_map[last_digit]"""
