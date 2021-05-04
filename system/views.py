from django.shortcuts import render

# from django.http import HttpResponse , HttpResponseRedirect
from .forms import CarForm, SaleOrderForm
# ShowroomForm,  FeedbackForm
from .models import Car, SaleOrder, Showroom

# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from django.contrib import auth
# from Accounts.models import Person, Employee, Customer

from system.extra_functionalities import check_booking_availability

def home(request):
    cars = Car.objects.all()
    context = {
        "title" : "Welcome to Car Rental",
        "cars" : cars
    }
    # print(cars)
    return render(request,'system/home.html', context)

def all_cars(request):
    cars = Car.objects.filter(available="Available")
    context = {
        "title" : "Check Variety of Cars",
        "cars" : cars
    }
    return render(request,'system/all_cars.html', context)

def car(request,id):
    cars = Car.objects.filter(id=id)
    cars = cars[0]
    context = {
        "title" : "Car",
        "car" : cars
    }
    return render(request,'system/car.html', context)

def all_showrooms(request):
    showrooms = Showroom.objects.all()
    context = {
        "title" : "View All Showrooms",
        "showrooms" : showrooms
    }
    return render(request,'system/all_showrooms.html', context)

def search_car(request):
    # car = Car.objects.all()
    
    bookings = SaleOrder.objects.all()

    if request.method == "POST":
        
        print('this is a POST Request')
        # form = CarForm(request.POST or None, request.FILES or None)
        print(request.POST.get('picking_address'))
        print(request.POST.get('picking_date'))
        print(request.POST.get('return_date'))

        
        # cars = Car.objects.all()
        search_parameters={
            "picking_address": request.POST.get('picking_address'),
            "picking_date":request.POST.get('picking_date'),
            "return_date":request.POST.get('return_date'),
        }
        # res = check_booking_availability(SaleOrder,Car,search_parameters)
        # print("res",res)

    context = {
        "title" : "Search a Car",
        "message" : bookings
    }
    return render(request,'system/search_car.html', context)

def add_new_car(request):
    
    if request.method == "POST":
        
        # print('this is a POST Request')
        form = CarForm(request.POST or None, request.FILES or None)
        # print(request.POST)
        # print(request.FILES)
        # print(request.FILES.get('car_photo'))
        
        if form.is_valid():
            car_name = form.cleaned_data['car_name']
            # print(car_name)
            car_photo = form.cleaned_data['car_photo']
            # print(car_photo)
            form.save()
            context = {
                "title" : "Add a Car",
                "message" : "Success",
            }
        else:
            print('invalid',form.errors.as_data())
            context = {
            "title" : "Adding a Car",
            "form" : CarForm,
            "message" : "",}
    else:
        context = {
        "title" : "Add a Car",
        "form" : CarForm,
        "message" : " ",
    }

    return render(request,'system/add_new_car.html', context)

