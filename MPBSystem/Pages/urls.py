import urllib
from django.urls import path, include
from django.contrib import admin
from .views import Home, Login, adminpanel, admindashboard, adminusers, Logout, Signup, Profile, Loans, Payment, PersonalLoan, StudentLoan, BusinessLoan, VehicleLoan, AgricultureLoan, GoldLoan, PawnBrokerism, MyPayments, Refinance, EMICalculator, Licensing, AboutUs, Contactus

urlpatterns = [
    path('Admin/', admin.site.urls),
    path('', Home, name='Home'),
    path('Login/', Login, name='Login'),
    path('adminpanel/', adminpanel, name='adminpanel'),
    path('admindashboard/', admindashboard, name='admindashboard'),
    path('adminusers/', adminusers, name='admindashboard'),
    path('Logout/', Logout, name='Logout'),
    path('Signup/', Signup, name='Signup'),
    path('Profile/', Profile, name='Profile'),
    path('Loans/', Loans, name='Loans'),
    path('Payment/', Payment, name='Payment'),
    path('PersonalLoan/', PersonalLoan, name='PersonalLoan'),
    path('StudentLoan/', StudentLoan, name='StudentLoan'),
    path('BusinessLoan/', BusinessLoan, name='BusinessLoan'),
    path('VehicleLoan/', VehicleLoan, name='VehicleLoan'),
    path('AgricultureLoan/', AgricultureLoan, name='AgricultureLoan'),
    path('GoldLoan/', GoldLoan, name='GoldLoan'),
    path('MyPayments/', MyPayments, name='Payments'),
    path('PawnBrokerism/', PawnBrokerism, name='PawnBrokerism'),
    path('Refinance/', Refinance, name='Refinance'),
    path('EMICalculator/', EMICalculator, name='EMICalculator'),
    path('Licensing/', Licensing, name='Licensing'),
    path('AboutUs/', AboutUs, name='AboutUs'),
    path('Contactus/', Contactus, name='Contactus'),
]
