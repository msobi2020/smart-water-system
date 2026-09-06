from django.shortcuts import render, redirect
from .models import Meter
from .forms import MeterForm


def meter_list(request):
    meters = Meter.objects.all()
    return render(request, 'meters/meter_list.html', {'meters': meters})


def add_meter(request):
    if request.method == 'POST':
        form = MeterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meter_list')
    else:
        form = MeterForm()
    return render(request, 'meters/add_meter.html', {'form': form})
