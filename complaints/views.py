from django.shortcuts import render, redirect
from .models import Complaint
from .forms import ComplaintForm


def complaint_list(request):
    complaints = Complaint.objects.all().order_by('-date_submitted')
    return render(request, 'complaints/complaint_list.html', {'complaints': complaints})


def add_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaint_list')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/add_complaint.html', {'form': form})
