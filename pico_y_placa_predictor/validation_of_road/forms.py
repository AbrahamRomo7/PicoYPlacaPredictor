from django import forms
from django.core.exceptions import ValidationError

from pico_y_placa_predictor.license_plate_number.validators import validate_license_plate

class LicensePlateForm(forms.Form):
    plate = forms.CharField(max_length=8, min_length=7,  
    widget=forms.TextInput(attrs={'placeholder': 'TDD-314', 'class': 'form-control'}), 
    error_messages={
        'required': 'License plate number is required',
        'max_length': '8 characters maximum',
        'min_length': '7 characteres minimum',
    })
    date = forms.DateField(max_length=10, min_length=10,
                           input_formats=['%Y-%m-%d'],
                            error_messages={'invalid': 'Format AAAA-MM-DD'})
    hour = forms.TimeField(
            error_messages={'required': 'Select an hour'})
    def validate_plate(self):
        plate = self.cleaned_data.get('plate')
        if plate:
            validate_license_plate(plate)
        return plate

