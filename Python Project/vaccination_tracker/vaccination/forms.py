from django import forms
from .models import VaccinationRecord

class VaccinationRecordForm(forms.ModelForm):
    class Meta:
        model = VaccinationRecord
        fields = ['child', 'vaccine_type', 'dose_number']
