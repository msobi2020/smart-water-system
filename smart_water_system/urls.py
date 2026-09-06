from django.contrib import admin
from django.urls import path
from core import views as core_views
from customers import views as customer_views
from meters import views as meter_views
from billing import views as billing_views
from complaints import views as complaint_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('login/', core_views.customer_login, name='login'),
    path('logout/', core_views.customer_logout, name='logout'),
    path('dashboard/', core_views.customer_dashboard, name='customer_dashboard'),
    path('customers/', customer_views.customer_list, name='customer_list'),
    path('customers/add/', customer_views.add_customer, name='add_customer'),
    path('meters/', meter_views.meter_list, name='meter_list'),
    path('meters/add/', meter_views.add_meter, name='add_meter'),
    path('bills/', billing_views.bill_list, name='bill_list'),
    path('bills/add/', billing_views.add_bill, name='add_bill'),
    path('bills/payment/add/', billing_views.add_payment, name='add_payment'),
    path('complaints/', complaint_views.complaint_list, name='complaint_list'),
    path('complaints/add/', complaint_views.add_complaint, name='add_complaint'),
    path('register/', core_views.register, name='register'),
]