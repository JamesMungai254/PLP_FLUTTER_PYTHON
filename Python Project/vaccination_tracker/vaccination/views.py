

# Create your views here.
from django.shortcuts import render, redirect
from .forms import VaccinationRecordForm
from .models import VaccinationRecord, Child

def record_list(request):
    # Initialize records as an empty list
    records = []

    # Check if the user is a parent
    if request.user.is_authenticated:
        if request.user.is_parent:
            # Fetch records for the parent user
            records = VaccinationRecord.objects.filter(child__parent__user=request.user)
        elif request.user.is_facilitator:
            # Fetch all vaccination records for facilitators
            records = VaccinationRecord.objects.all()
    
    return render(request, 'vaccination/record_list.html', {'records': records})

def add_record(request):
    if request.method == 'POST':
        form = VaccinationRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vaccination:record_list')
    else:
        form = VaccinationRecordForm()
    return render(request, 'vaccination/record_detail.html', {'form': form})
