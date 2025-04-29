from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

class Login(LoginView):
    template_name = 'login.html'


def home(request):
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
