from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import requests
import os
import logging
from dotenv import load_dotenv
import json

from toka.forms import LoginForm, SignupForm

def home(request):
    return render(request, 'index.html')

def workouts(request):
    return "hello"

def nutrition(request):
    return "hello"

def community(request):
    return "hello"

# login view 
def login_view(request):
    if request.user.is_authenticated:
        print("already logged in")
        return HttpResponseRedirect("/")

    login_form = LoginForm(request.POST or None)
    error_message = None

    if request.method == "POST":
        if login_form.is_valid():
            authenticated_user = authenticate(
                request, 
                username=login_form.cleaned_data.get("username"), 
                password=login_form.cleaned_data.get("password")
            )
            if authenticated_user is not None:
                login(request, authenticated_user)
                return HttpResponseRedirect("/")
            else:
                error_message = "Invalid username or password."
        else:
            print(login_form.errors)
    print(error_message)
    return render(request, 'login.html', {'login_form': login_form, 'error_message': error_message})

def signup_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")

    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            # Create a new user
            user = User.objects.create_user(
                username=signup_form.cleaned_data.get("username"),
                email=signup_form.cleaned_data.get("email"),
                password=signup_form.cleaned_data.get("password")
            )
            authenticated_user = authenticate(
                request,
                username=signup_form.cleaned_data.get("username"), 
                password=signup_form.cleaned_data.get("password")
            )
            if authenticated_user is not None:
                login(request=request, user=authenticated_user)
                return HttpResponseRedirect("/")
        else:
            return render(request, 'signup.html', {'signup_form': signup_form, 'errors': signup_form.errors})

    else:
        signup_form = SignupForm()

    return render(request, 'signup.html', {'signup_form': signup_form})
