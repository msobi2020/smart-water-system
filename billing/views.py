from django.shortcuts import render, redirect
from .models import Bill, Payment
from .forms import BillForm, PaymentForm


def bill_list(request):
    bills = Bill.objects.all().order_by('-date_generated')
    return render(request, 'billing/bill_list.html', {'bills': bills})


def add_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillForm()
    return render(request, 'billing/add_bill.html', {'form': form})


def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            payment.bill.status = 'paid'
            payment.bill.save()
            return redirect('bill_list')
    else:
        form = PaymentForm()
    return render(request, 'billing/add_payment.html', {'form': form})
