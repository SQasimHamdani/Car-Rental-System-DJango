from django.shortcuts import render, redirect
# import datetime
from datetime import datetime,date, timedelta

from django.http import HttpResponseRedirect
from .forms import CarForm, SaleOrderForm, ShowroomForm
# ShowroomForm,  FeedbackForm
from .models import Car, SaleOrder, Showroom

# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
from django.contrib import auth
# from Accounts.models import Person, Employee, Customer
from Accounts.models import Person, Customer

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

    booked_cars = Car.objects.filter(available="Booked")
    
    for booked_car in booked_cars:
        stat=[]
        # print(booked_car)
        bookings = SaleOrder.objects.filter(car=booked_car.id)
        # print("time now",datetime.now().strftime('%Y.%m.%d'))
        for booking in bookings:
            # print(booking.Deliver_Date.strftime('%Y.%m.%d'))
            # print(datetime.now().strftime('%Y.%m.%d'))
            if booking.Deliver_Date.strftime('%Y.%m.%d') < datetime.now().strftime('%Y.%m.%d'):
                stat.append(True)
                # booked_car.save()
            else:
                stat.append(False)
        if all(stat):
            booked_car.available = "Available"
            booked_car.save()

    if request.method == "POST":
        showroom_id = request.POST.get('showroom_cars')
        cars = Car.objects.filter(available="Available", showroom=showroom_id)
    else:
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

def add_new_showroom(request):
    if request.method == "POST":
        
        # print('this is a POST Request')
        form = ShowroomForm(request.POST or None, request.FILES or None)
        # print(request.POST)
        # print(request.FILES)
        # print(request.FILES.get('car_photo'))
        
        if form.is_valid():
            # car_name = form.cleaned_data['car_name']
            # print(car_name)
            # car_photo = form.cleaned_data['car_photo']
            # print(car_photo)
            form.save()
            context = {
                "title" : "Add a Showroom",
                "message" : "Success",
            }
        else:
            # print('invalid',form.errors.as_data())
            context = {
            "title" : "Adding a Showroom",
            "form" : ShowroomForm,
            "message" : "Error while creating showroom - Try choosing a unique different name",
            }
    else:
        context = {
        "title" : "Add a Showroom",
        "form" : ShowroomForm,
        "message" : " ",
    }

    return render(request,'system/add_new_showroom.html', context)

def search_car(request):
    # car = Car.objects.all()
    
    # bookings = SaleOrder.objects.all()

    if request.method == "POST":
        
        print('this is a POST Request')
        # form = CarForm(request.POST or None, request.FILES or None)
        # print(request.POST.get('picking_address'))
        # print(request.POST.get('picking_date'))
        # print(request.POST.get('return_date'))

        
        # cars = Car.objects.all()
        # search_parameters={
        #     "picking_address": request.POST.get('picking_address'),
        #     "picking_date":request.POST.get('picking_date'),
        #     "return_date":request.POST.get('return_date'),
        # }
        # res = check_booking_availability(SaleOrder,Car,search_parameters)
        # print("res",res)

    context = {
        "title" : "Search a Car",
        # "message" : bookings
    }
    return render(request,'system/search_car.html', context)

def add_new_car(request):
    showrooms = Showroom.objects.all()
    if request.method == "POST":
        
        # print('this is a POST Request')
        form = CarForm(request.POST or None, request.FILES or None)
        # print(request.POST)
        # print(request.FILES)
        # print(request.FILES.get('car_photo'))
        
        if form.is_valid():
            # car_name = form.cleaned_data['car_name']
            # print(car_name)
            # car_photo = form.cleaned_data['car_photo']
            # print(car_photo)
            form.save()
            context = {
                "title" : "Add a Car",
                "message" : "Success",
                "showrooms" : showrooms,
            }
        else:
            # print('invalid',form.errors.as_data())
            context = {
            "title" : "Adding a Car",
            "form" : CarForm,
            "message" : form.errors.as_data(),
            "showrooms" : showrooms,
            }
    else:
        context = {
        "title" : "Add a Car",
        "form" : CarForm,
        "message" : " ",
        "showrooms" : showrooms,
    }

    return render(request,'system/add_new_car.html', context)

def book_a_car(request,id):
    message = ""
    if not request.user.is_authenticated:
        message="Error - Register yourself First"
    
        context = {
            "title" : "Login",
            "message" : message,
        }
        return HttpResponseRedirect('/login',context)

    if request.method == "GET" or ( request.method == "POST" and request.POST.get('book_view')=="book_page"):
        
        # car = Car.objects.filter(id=id)[0]
        context = {
            "title" : "Confirm Car Booking",
            "message" : "Confirm Car Booking",
            # "car" : car
        }
        
        return render(request,'system/book.html', context)

    elif request.method == "POST":
        
        # print('this is a POST Request')
        # form = CarForm(request.POST or None, request.FILES or None)
        # print(request.POST.get('picking_address'))
        # print(request.POST.get('picking_date'))
        picking_date= request.POST.get('picking_date')
        # picking_date = picking_date +"."+ str(datetime.now().strftime('%D.%m.%Y').split(".")[2])
        
        # picking_date = date_converter.date_to_datetime(picking_date)
        picking_date = picking_date.split(".")
        # picking_date = datetime.strptime(picking_date, '%m.%d.%Y')
        # picking_date = date(int(picking_date[2]), int(picking_date[0]), int(picking_date[1]))
        # picking_date = date_converter.date_to_datetime(picking_date)
        picking_date = date(int(picking_date[2]), int(picking_date[1]), int(picking_date[0]))
        
        # print
        

        print("picking_date",picking_date.strftime('%Y.%m.%d'))
        print("time now",datetime.now().strftime('%Y.%m.%d'))

        # picking_date = datetime.strptime(str(picking_date), '%Y-%m-%d %H:%i:%s')
        
        
        return_date= request.POST.get('return_date')
        # return_date = return_date +"."+ str(datetime.now().strftime('%D.%m.%Y').split(".")[2])
        return_date = return_date.split(".")
        return_date = date(int(return_date[2]), int(return_date[1]), int(return_date[0]))
        
        print("return_date",return_date.strftime('%Y.%m.%d'))

        if picking_date.strftime('%Y.%m.%d') < datetime.now().strftime('%Y.%m.%d'):
            context = {
                "title" : "Car Booking",
                "message" : "Error in Date- Add Current or Future Date",
                # "car" : car
            }
            return render(request,'system/book.html', context)
        
        if picking_date.strftime('%Y.%m.%d') > return_date.strftime('%Y.%m.%d'):
            context = {
                "title" : "Car Booking",
                "message" : "Error in Date- Return Date Should be Afterwards",
                # "car" : car
            }
            return render(request,'system/book.html', context)
        
        # print(request.POST.get('return_date'))
        # print(request.POST.get('return_date'))
        # print(id)

        to_register_days = return_date - picking_date
        # print(to_register_days)
        if str(to_register_days) == "0:00:00":
            # to_register_days += 1
            return_date += timedelta(days=1)
            print(return_date)

        car = Car.objects.filter(id=id)[0]
        # print(car.showroom)

        person = Person.objects.filter(customer=request.user.id)[0]
        # print(customer.name)
        customer = Customer.objects.filter(customer=person)[0]
        if not car.available == "Booked":
            booking_form = SaleOrder(
                customer = customer,
                showroom = car.showroom,
                car = car,
                address = request.POST.get('picking_address'),
                Order_Date = picking_date,
                Deliver_Date = return_date,
            )
            booking_form.save()
            car.available = "Booked"
            car.save()
        

            context = {
                "title" : "Booking Confirmed",
                "message" : "Success - Booking Confirmed",
                # "car" : car
            }
        else:
            context = {
                "title" : "Car not Available",
                "message" : "Error Booking- Car not Available",
                # "car" : car
            }
        return render(request,'system/book.html', context)
