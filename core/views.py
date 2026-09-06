from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from customers.models import Customer
from meters.models import Meter
from billing.models import Bill
from complaints.models import Complaint


def home(request):
    context = {
        'total_customers': Customer.objects.count(),
        'total_meters': Meter.objects.count(),
        'unpaid_bills': Bill.objects.filter(status='unpaid').count(),
        'open_complaints': Complaint.objects.filter(status='open').count(),
    }
    return render(request, 'home.html', context)


def customer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('customer_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Jina au nenosiri si sahihi'})
    return render(request, 'login.html')


def customer_logout(request):
    logout(request)
    return redirect('home')


@login_required
def customer_dashboard(request):
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        return redirect('home')

    meters = Meter.objects.filter(customer=customer)
    bills = Bill.objects.filter(meter__customer=customer).order_by('-date_generated')
    complaints = Complaint.objects.filter(customer=customer).order_by('-date_submitted')

    context = {
        'customer': customer,
        'meters': meters,
        'bills': bills,
        'complaints': complaints,
    }
    return render(request, 'customer_dashboard.html', context)