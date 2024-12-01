from django.db import models
from accounts.models import Parent 
# Create your models here.


class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    
    

class VaccinationRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='vaccination_records')
    vaccine_type = models.CharField(max_length=100)
    dose_number = models.IntegerField()
    date_administered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.vaccine_type} - Dose {self.dose_number} for {self.child.full_name} on {self.date_administered}"
