from django.core.exceptions import ValidationError
import re

def validate_license_plate(plate):

    if not isinstance(plate, str):
        raise ValidationError('Invalid License plate number format')

    if len(plate) < 7 or len(plate) > 8:
        raise ValidationError('Invalid License plate number format')

    pattern = r'^[A-Z]{3}-\d{3,4}$'
    
    if not re.match(pattern, plate):
        raise ValidationError('Invalid License plate number format')

    return plate
