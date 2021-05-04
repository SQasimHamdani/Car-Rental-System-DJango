from django.shortcuts import render

from django.http import HttpResponse , HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from Accounts.models import Person, Employee, Customer


def login(request):
    message = ""
    if request.user.is_authenticated:
        return HttpResponseRedirect('/all_cars')

    if request.method == "POST":
        print('this is a POST Request')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        auth.login(request, user)
        # try:
        #     customer = Customer.objects.get(user = user)
        # except:
        #     customer = None
        # if customer is not None:
        #     auth.login(request, user)
        #     return render(request, 'customer/home_page.html')
        # else:
        #     return render(request, 'customer/login_failed.html')
        message = "Success"

        context = {
            "title" : "Login",
            "message" : message,
        }
        return HttpResponseRedirect('all_cars',context)

    context = {
        "title" : "Login",
        "message" : message,
    }
    return render(request, 'Accounts/login.html', context)


def signout(request):
    message = ""
    if request.user.is_authenticated:
        auth.logout(request)
        message="Success - Signout"
    
    context = {
        "title" : "Login",
        "message" : message,
    }
    return HttpResponseRedirect('login',context)

def register(request):
    
    if request.method == "POST":
        
        print('this is a POST Request')
        

        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        works_at_showroom = request.POST.get('works_at_showroom')

        print(request.POST.get('name'))
        print(request.POST.get('address'))
        print(request.POST.get('phone'))
        print(request.POST.get('username'))
        print(request.POST.get('email'))
        print(request.POST.get('password'))
        print(request.POST.get('works_at_showroom'))

        try:
            user = User.objects.create_user(username = username, password = password, email = email)
            user.name = name
            user.save()
        except:
            print("Error when creating user")
            context = {
                "title" : "register",
                "message" : "Error when creating user",
            }
            return render(request, 'Accounts/register.html', context)
        
        try:
            person = Person(  
                            # username = username, 
                            # password = password, 
                            # email = email,
                            person = user,
                            name = name,
                            address = address,
                            phone = phone,
                            )
            person.save()
        except:
            print("Error when creating Person")
            context = {
                "title" : "register",
                "message" : "Error when creating Person",
            }
            return render(request, 'Accounts/register.html', context)
            

        try:
            customer = Customer(customer = person)
            customer.save()
        except:
            print("Error when creating customer")
            context = {
                "title" : "register",
                "message" : "Error when creating customer",
            }
            return render(request, 'Accounts/register.html', context)
        
        print("Success")
        context = {
            "title" : "register",
            "message" : "Success",
        }
        return render(request, 'Accounts/register.html', context)

    else:
        context = {
            "title" : "register",
        }

        return render(request,'Accounts/register.html', context)