from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from datetime import date


# Create your views here.
def Home(request):
    return render(request, 'Home.html')


def Signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if User.objects.filter(username=username).exists():
            messages.error(request, '⚠️Username already taken! Choose a different one.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, '⚠️E-mail already exists! Use a different email.')
        elif password == password_confirm:
            user = User.objects.create_user(username, email, password)
            user.save()
            messages.success(request, 'User Created Successfully!✅')
            return redirect('Login')
        else:
            messages.error(request, '⚠️Password and Confirm Password do not match!')
    return render(request, 'Signup.html')


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('Home')
        else:
            messages.error(request, '⚠️Invalid username or password. Please try again!')
            return render(request, 'Login.html')
    return render(request, 'Login.html')


def Logout(request):
    auth.logout(request)
    messages.success(request, "Log Out Successful.✅")
    return redirect('Login')


def Profile(request):
    if request.user.is_authenticated:
        return render(request, 'Profile.html')
    else:
        messages.error(request, "⚠️Please Login to view your Profile.")
        return redirect('Login')


def Loans(request):
    return render(request, 'Loans.html')


def Payment(request):
    if request.user.is_authenticated:
        return render(request, 'Payment.html')
    else:
        messages.error(request, "⚠️Please Login to Continue to Payment")
        return redirect('/Login')


def PersonalLoan(request):
    return render(request, 'PersonalLoan.html')


def StudentLoan(request):
    return render(request, 'StudentLoan.html')


def BusinessLoan(request):
    return render(request, 'BusinessLoan.html')


def VehicleLoan(request):
    return render(request, 'VehicleLoan.html')


def AgricultureLoan(request):
    return render(request, 'AgricultureLoan.html')


def GoldLoan(request):
    return render(request, 'GoldLoan.html')


def PawnBrokerism(request):
    return render(request, 'PawnBrokerism.html')


def MyPayments(request):
    return render(request, 'MyPayments.html')


def Refinance(request):
    return render(request, 'Refinance.html')


def EMICalculator(request):
    return render(request, 'EMICalculator.html')


def Licensing(request):
    return render(request, 'Licensing.html')


def AboutUs(request):
    return render(request, 'AboutUs.html')


def Contactus(request):
    return render(request, 'Contactus.html')


@staff_member_required(login_url='/adminpanel')
def adminpanel(request):
    if request.user.is_authenticated:
        return render(request, 'adminpanel.html')


@staff_member_required(login_url='/adminpanel')
def admindashboard(request):
    Dashboard = User.objects.all()
    return render(request, 'admindashboard.html', {"Dashboard": Dashboard})


@staff_member_required(login_url='/adminpanel')
def adminusers(request):
    displaynames = User.objects.all()
    return render(request, 'adminusers.html', {"displaynames": displaynames})