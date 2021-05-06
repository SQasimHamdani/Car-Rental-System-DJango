from django.urls import path,include
from django.contrib import admin
from system import views

urlpatterns = [
    path('', views.home, name = "home"),

    path('all_cars', views.all_cars, name = "all_cars"),
    path('car/<id>', views.car, name='car_view'),

    path('search_car', views.search_car, name = "search_car"),
    path('add_new_car', views.add_new_car, name = "add_new_car"),
    path('all_showrooms', views.all_showrooms, name = "all_showrooms"),
    path('car/<id>/book', views.book_a_car, name = "book_a_car"),
]