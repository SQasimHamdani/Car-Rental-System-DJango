from django.shortcuts import render

# Create your views here.
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
)

