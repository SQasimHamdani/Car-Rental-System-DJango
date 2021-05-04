from django.urls import path,include
from django.contrib import admin
from Accounts import views
    

urlpatterns = [
    path('login', views.login, name = "login"),
    path('register', views.register, name = "register"),
    path('signout', views.signout, name = "signout"),
]